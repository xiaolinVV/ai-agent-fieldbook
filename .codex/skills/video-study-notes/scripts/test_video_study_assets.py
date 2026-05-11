import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import video_study_assets as assets


class AsrFallbackTests(unittest.TestCase):
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

            def fake_run(cmd, check=True):
                calls.append(cmd)
                if cmd[0] == "ffmpeg":
                    Path(cmd[-1]).write_bytes(b"wav")
                if cmd[0] == "whisper-cli":
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
            self.assertEqual(calls[1][0], "whisper-cli")
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


if __name__ == "__main__":
    unittest.main()
