import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import video_study_assets as assets


class AsrFallbackTests(unittest.TestCase):
    def test_whisper_cli_path_finds_project_local_ubuntu_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local_cli = root / "local-media/tools/whisper.cpp/build/bin/whisper-cli"
            local_cli.parent.mkdir(parents=True)
            local_cli.write_text("#!/bin/sh\n", encoding="utf-8")
            local_cli.chmod(0o755)

            with mock.patch.object(assets, "which", return_value=None):
                path = assets.whisper_cli_path(root)

            self.assertEqual(path, str(local_cli))

    def test_whisper_cli_path_prefers_homebrew_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local_cli = root / "local-media/tools/whisper.cpp/build/bin/whisper-cli"
            local_cli.parent.mkdir(parents=True)
            local_cli.write_text("#!/bin/sh\n", encoding="utf-8")
            local_cli.chmod(0o755)

            def fake_which(name):
                return "/opt/homebrew/bin/whisper-cli" if name == "whisper-cli" else None

            with mock.patch.object(assets, "which", side_effect=fake_which):
                path = assets.whisper_cli_path(root)

            self.assertEqual(path, "/opt/homebrew/bin/whisper-cli")

    def test_whisper_runtime_env_leaves_homebrew_install_unchanged(self):
        base_env = {"DYLD_LIBRARY_PATH": "/existing"}

        env = assets.whisper_runtime_env("/opt/homebrew/bin/whisper-cli", base_env)

        self.assertEqual(env, base_env)

    def test_whisper_runtime_env_adds_local_shared_library_dirs(self):
        with tempfile.TemporaryDirectory() as tmp:
            cli = Path(tmp) / "local-media/tools/whisper.cpp/build/bin/whisper-cli"
            cli.parent.mkdir(parents=True)
            build = cli.parents[1]
            (build / "src").mkdir()
            (build / "ggml/src").mkdir(parents=True)

            env = assets.whisper_runtime_env(str(cli), {"LD_LIBRARY_PATH": "/existing"})

            expected = f"{build / 'src'}:{build / 'ggml/src'}:/existing"
            self.assertEqual(env["LD_LIBRARY_PATH"], expected)

    def test_whisper_runtime_env_uses_dyld_library_path_on_macos_local_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            cli = Path(tmp) / "local-media/tools/whisper.cpp/build/bin/whisper-cli"
            cli.parent.mkdir(parents=True)
            build = cli.parents[1]
            (build / "src").mkdir()
            (build / "ggml/src").mkdir(parents=True)

            with mock.patch.object(assets.sys, "platform", "darwin"):
                env = assets.whisper_runtime_env(str(cli), {"DYLD_LIBRARY_PATH": "/existing"})

            expected = f"{build / 'src'}:{build / 'ggml/src'}:/existing"
            self.assertEqual(env["DYLD_LIBRARY_PATH"], expected)
            self.assertNotIn("LD_LIBRARY_PATH", env)

    def test_detect_proxy_uses_macos_scutil_when_no_env_proxy(self):
        scutil = "\n".join([
            "HTTPSEnable : 1",
            "HTTPSProxy : 127.0.0.1",
            "HTTPSPort : 7890",
        ])

        with mock.patch.dict(assets.os.environ, {}, clear=True):
            with mock.patch.object(assets.sys, "platform", "darwin"):
                with mock.patch.object(assets, "which", return_value="/usr/sbin/scutil"):
                    with mock.patch.object(assets, "run", return_value=mock.Mock(returncode=0, stdout=scutil)):
                        proxy = assets.detect_proxy("auto")

        self.assertEqual(proxy, "http://127.0.0.1:7890")

    def test_asr_output_base_strips_quicktime_suffix(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            video = directory / "Demo Video [abc123].quicktime.mp4"
            video.write_bytes(b"video")

            output_base = assets.asr_output_base(directory)

            self.assertEqual(output_base, directory / "Demo Video [abc123].zh-Hans")

    def test_run_asr_fallback_builds_audio_and_whisper_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "Demo Video [abc123].quicktime.mp4").write_bytes(b"video")
            model = directory / "ggml-base-q5_1.bin"
            model.write_bytes(b"model")
            calls = []

            def fake_run(cmd, check=True, env=None):
                calls.append(cmd)
                if cmd[0] == "ffmpeg":
                    Path(cmd[-1]).write_bytes(b"wav")
                if Path(cmd[0]).name == "whisper-cli":
                    output_base = Path(cmd[cmd.index("-of") + 1])
                    Path(f"{output_base}.srt").write_text("1\n00:00:00,000 --> 00:00:01,000\ntext\n", encoding="utf-8")
                return mock.Mock(returncode=0, stdout="", stderr="")

            with mock.patch.object(assets, "which", return_value="/usr/local/bin/whisper-cli"):
                with mock.patch.object(assets, "run", side_effect=fake_run):
                    subtitle = assets.run_asr_fallback(
                        directory=directory,
                        proxy=None,
                        force=True,
                        model_name="base-q5_1",
                        model_path=model,
                        download_model=False,
                        threads=2,
                        processors=3,
                    )

            self.assertEqual(subtitle, directory / "Demo Video [abc123].zh-Hans.srt")
            self.assertEqual(calls[0][0], "ffmpeg")
            self.assertEqual(calls[0][-1], str(directory / "audio-16k.wav"))
            self.assertEqual(calls[1][0], "/usr/local/bin/whisper-cli")
            self.assertIn(str(model), calls[1])
            self.assertIn("-bs", calls[1])
            self.assertIn("1", calls[1])
            self.assertIn("-bo", calls[1])
            self.assertIn("-osrt", calls[1])
            self.assertIn("-ovtt", calls[1])
            self.assertIn("-otxt", calls[1])
            self.assertIn("-oj", calls[1])
            self.assertEqual(calls[1][calls[1].index("-t") + 1], "2")
            self.assertEqual(calls[1][calls[1].index("-p") + 1], "3")

    def test_manifest_marks_local_asr_when_info_has_no_caption_tracks(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            info = {
                "title": "Demo",
                "channel": "Channel",
                "upload_date": "20250102",
                "duration": 61,
                "subtitles": {},
                "automatic_captions": {},
            }
            (directory / "Demo [abc123].quicktime.info.json").write_text(json.dumps(info), encoding="utf-8")
            (directory / "Demo [abc123].quicktime.mp4").write_bytes(b"video")
            subtitle = directory / "Demo [abc123].zh-Hans.srt"
            subtitle.write_text("1\n00:00:00,000 --> 00:00:01,000\ntext\n", encoding="utf-8")

            manifest = assets.write_manifest(
                directory=directory,
                url="https://example.test/video",
                slug="demo",
                proxy=None,
                clean_path=None,
                chapter_path=None,
                contact=None,
                comments_json=None,
                comments_digest=None,
                comments=[],
            )

            text = manifest.read_text(encoding="utf-8")
            self.assertIn("subtitle_source: local ASR fallback or manually supplied subtitle", text)

    def test_manifest_marks_forced_asr_subtitle_over_youtube_caption_tracks(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            info = {
                "title": "Demo",
                "channel": "Channel",
                "upload_date": "20250102",
                "duration": 61,
                "subtitles": {"en": [{"ext": "srt"}]},
                "automatic_captions": {},
            }
            (directory / "Demo [abc123].quicktime.info.json").write_text(json.dumps(info), encoding="utf-8")
            (directory / "Demo [abc123].quicktime.mp4").write_bytes(b"video")
            subtitle = directory / "Demo [abc123].zh-Hans.srt"
            subtitle.write_text("1\n00:00:00,000 --> 00:00:01,000\ntext\n", encoding="utf-8")
            (directory / "Demo [abc123].zh-Hans.txt").write_text("text\n", encoding="utf-8")
            (directory / "Demo [abc123].zh-Hans.json").write_text("{}", encoding="utf-8")

            manifest = assets.write_manifest(
                directory=directory,
                url="https://example.test/video",
                slug="demo",
                proxy=None,
                clean_path=None,
                chapter_path=None,
                contact=None,
                comments_json=None,
                comments_digest=None,
                comments=[],
            )

            text = manifest.read_text(encoding="utf-8")
            self.assertIn("subtitle_source: local ASR fallback or manually supplied subtitle", text)


class CodeUrlTests(unittest.TestCase):
    def test_collect_description_urls_ignores_ytdlp_direct_media_url(self):
        info = {
            "description": "See https://example.com/notes",
            "webpage_url": "https://www.youtube.com/watch?v=abc123",
            "original_url": "https://www.youtube.com/watch?v=abc123",
            "url": "https://rr4---sn.example.googlevideo.com/videoplayback?source=youtube",
        }

        urls = assets.collect_description_urls(info, "https://www.youtube.com/watch?v=abc123")

        self.assertIn("https://example.com/notes", urls)
        self.assertIn("https://www.youtube.com/watch?v=abc123", urls)
        self.assertNotIn(info["url"], urls)

    def test_googlevideo_download_url_is_not_code_link(self):
        url = "https://rr4---sn.example.googlevideo.com/videoplayback?source=youtube&mime=video%2Fmp4"

        self.assertFalse(assets.is_code_or_project_url(url))

    def test_known_code_hosts_are_code_links(self):
        self.assertTrue(assets.is_code_or_project_url("https://github.com/example/project"))
        self.assertTrue(assets.is_code_or_project_url("https://huggingface.co/example/model"))


if __name__ == "__main__":
    unittest.main()
