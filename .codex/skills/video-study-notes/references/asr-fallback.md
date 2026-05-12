# ASR Fallback For Missing YouTube Caption Tracks

Use this when the browser appears to show captions but `yt-dlp` cannot download or list standard subtitle tracks.

## Diagnosis

Run the normal capture first. If `asset-manifest.md` says `subtitle: missing`, verify whether YouTube exposed any standard tracks:

```bash
yt-dlp --ignore-config --proxy http://127.0.0.1:PORT --list-subs 'VIDEO_URL'
yt-dlp --ignore-config --proxy http://127.0.0.1:PORT --cookies-from-browser chrome --list-subs 'VIDEO_URL'
```

If both return `has no automatic captions` and `has no subtitles`, do not keep fighting the YouTube subtitle path. Browser-visible captions may be live captions, account/region/client experiments, or UI features that are not exposed as downloadable caption tracks.

## Environment Setup

macOS with Homebrew:

```bash
brew install yt-dlp ffmpeg whisper-cpp
python3 .codex/skills/video-study-notes/scripts/video_study_assets.py preflight
```

Ubuntu with sudo:

```bash
sudo apt update
sudo apt install -y git cmake build-essential
mkdir -p local-media/tools
git clone --depth 1 https://github.com/ggml-org/whisper.cpp local-media/tools/whisper.cpp
cmake -S local-media/tools/whisper.cpp -B local-media/tools/whisper.cpp/build \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_NATIVE=OFF \
  -DGGML_OPENMP=OFF
cmake --build local-media/tools/whisper.cpp/build --config Release -j"$(nproc)"
python3 .codex/skills/video-study-notes/scripts/video_study_assets.py preflight
```

Ubuntu without sudo but with Docker:

```bash
mkdir -p local-media/tools
git clone --depth 1 https://github.com/ggml-org/whisper.cpp local-media/tools/whisper.cpp
docker run --rm \
  -v "$PWD/local-media/tools/whisper.cpp:/src" \
  -w /src \
  ubuntu:24.04 \
  bash -lc 'apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ca-certificates cmake build-essential git && cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DGGML_NATIVE=OFF -DGGML_OPENMP=OFF && cmake --build build --config Release -j"$(nproc)"'
python3 .codex/skills/video-study-notes/scripts/video_study_assets.py preflight
```

Expected preflight basics:

- `yt-dlp`, `ffmpeg`, and `ffprobe` must exist.
- `whisper-cli` should exist for ASR fallback. The helper detects PATH plus local builds at `local-media/tools/whisper.cpp/build/bin/whisper-cli` and compatible older build paths.
- A local ASR model under `local-media/models/whisper.cpp/` is needed before ASR can run.
- For project-local Linux builds, run ASR through `video_study_assets.py`; it adds the local `libwhisper`/`libggml` directories to the runtime environment. A bare `local-media/tools/whisper.cpp/build/bin/whisper-cli` command may fail unless `LD_LIBRARY_PATH` is set.

`local-media/` should be ignored by Git. Keep Whisper binaries, models, generated audio, and downloaded media there.

## First ASR Run

Preferred first run:

```bash
python3 .codex/skills/video-study-notes/scripts/video_study_assets.py capture \
  'VIDEO_URL' \
  --slug 'YYYY-MM-DD-channel-topic' \
  --asr-download-model
```

This downloads media with `yt-dlp`, then runs ASR only if no subtitle is available. The default model is `base-q5_1`, stored at:

```text
local-media/models/whisper.cpp/ggml-base-q5_1.bin
```

If the video is already downloaded and only the transcript needs regeneration:

```bash
python3 .codex/skills/video-study-notes/scripts/video_study_assets.py capture \
  'VIDEO_URL' \
  --slug 'YYYY-MM-DD-channel-topic' \
  --skip-download \
  --asr-fallback force \
  --asr-download-model
```

Useful flags:

| Flag | Use |
|---|---|
| `--asr-fallback auto` | Default. Run ASR only when no subtitle exists and ASR dependencies are present. |
| `--asr-fallback force` | Regenerate ASR subtitle even if a subtitle already exists. |
| `--asr-fallback never` | Do not run ASR. Leave transcript missing if YouTube has no subtitles. |
| `--asr-model base-q5_1` | Recommended default for Chinese technical videos on Intel Macs. |
| `--asr-model small` | Better accuracy, much slower on CPU. |
| `--asr-model tiny` | Faster, lower Chinese/technical-term quality. |
| `--asr-model-path PATH` | Use a manually downloaded `ggml-*.bin` model. |
| `--asr-threads N --asr-processors N` | Tune CPU parallelism. Defaults are conservative. |

## Manual Model Download

If script download fails, download manually:

```bash
mkdir -p local-media/models/whisper.cpp
curl -L --fail -C - \
  -o local-media/models/whisper.cpp/ggml-base-q5_1.bin \
  'https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base-q5_1.bin'
```

Behind a local proxy:

```bash
curl -L --fail -C - --proxy http://127.0.0.1:PORT \
  -o local-media/models/whisper.cpp/ggml-base-q5_1.bin \
  'https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base-q5_1.bin'
```

## Generated Files

ASR writes files next to the video:

```text
audio-16k.wav
<video-title> [<id>].zh-Hans.srt
<video-title> [<id>].zh-Hans.vtt
<video-title> [<id>].zh-Hans.txt
<video-title> [<id>].zh-Hans.json
transcript-clean.txt
chapter-transcript.md
asset-manifest.md
```

`asset-manifest.md` should include:

```text
subtitle_source: local ASR fallback or manually supplied subtitle
```

## Note-Writing Rules For ASR Transcripts

- Do not call ASR output "official subtitles".
- Add a local asset note: `字幕说明：YouTube 对 yt-dlp 未暴露标准字幕轨道；此字幕由本地 whisper.cpp ASR 生成，未逐句人工校对。`
- Correct obvious ASR term errors in the study note, especially technical words like `Embedding`, `Vector`, `Recall`, `Re-ranking`, `Cross-Encoder`, `MTEB`.
- Do not paste ASR transcript verbatim. Summarize and transform.
- Add `未验证事项`: ASR transcript was not fully human-proofread.

## Failure Handling

- `yt-dlp` network timeout: verify proxy with `curl -I --proxy http://127.0.0.1:PORT 'https://www.youtube.com/watch?v=...'`.
- Browser shows captions but `yt-dlp` does not: treat as non-standard captions; use ASR.
- `whisper-cli` missing: install `whisper-cpp` on macOS, or build `whisper.cpp` locally under `local-media/tools/whisper.cpp/` on Ubuntu/Linux. If the machine lacks build tools and sudo, use the Docker build path above.
- Model missing and no network: keep assets and manifest, then report `transcript_clean: missing`; do not claim the video note is complete.
- ASR is too slow: try `--asr-model base-q5_1`; avoid `small` on older Intel CPUs unless accuracy matters more than time.
