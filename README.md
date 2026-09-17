# InstaDL

A lightweight Python CLI for downloading **public Instagram videos and Reels** in the highest quality available.

InstaDL uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to retrieve Instagram media and **FFmpeg** to merge the highest-quality video and audio streams when they are provided separately.

## Features

* Download public Instagram Reels and video posts
* Automatically select the highest-quality video stream
* Automatically select the highest-quality audio stream
* Merge separate video and audio streams into MP4
* Automatically detect the current Windows user
* Save downloads to the user's `Videos\instadl` directory
* Display download progress, speed, and ETA
* Retry temporary download failures
* Support direct URLs through command-line arguments
* Modular Python architecture
* Designed to work as a global Windows CLI command

## Project Structure

```text
instadl/
│
├── index.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── instadl/
    ├── __init__.py
    ├── config.py
    ├── downloader.py
    ├── progress.py
    └── validators.py
```

## Modules

| File                    | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| `index.py`              | Application entry point and CLI handling |
| `instadl/config.py`     | Download and yt-dlp configuration        |
| `instadl/downloader.py` | Instagram download logic                 |
| `instadl/progress.py`   | Download progress handling               |
| `instadl/validators.py` | Instagram URL validation                 |
| `instadl/__init__.py`   | Python package initialization            |

## Requirements

InstaDL requires:

* Python 3.10+
* yt-dlp
* FFmpeg

The project is currently designed primarily for **Windows**.

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/WissemHammami009/instadl.git
cd instadl
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents script execution, you can activate the environment from Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install Python dependencies

```powershell
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

The current `requirements.txt` contains:

```text
yt-dlp
```

## FFmpeg

FFmpeg is required when Instagram provides the highest-quality video and audio as separate streams.

On Windows, install FFmpeg with Winget:

```powershell
winget install --id Gyan.FFmpeg -e
```

Close and reopen your terminal after installation.

Verify that FFmpeg is available:

```powershell
ffmpeg -version
```

If the command displays FFmpeg version information, the installation is ready.

## Usage

### Interactive Mode

Run:

```powershell
py .\index.py
```

InstaDL will ask for an Instagram URL:

```text
Paste public Instagram Reel URL:
```

Paste a public Instagram Reel or video-post URL and press Enter.

### Command-Line Mode

You can also provide the URL directly:

```powershell
py .\index.py "https://www.instagram.com/reel/XXXXXXXXXXX/"
```

Regular public Instagram video posts are also supported when yt-dlp can extract them:

```powershell
py .\index.py "https://www.instagram.com/p/XXXXXXXXXXX/"
```

## Download Location

InstaDL automatically detects the currently logged-in Windows user's home directory.

Downloads are stored in:

```text
C:\Users\<USERNAME>\Videos\instadl
```

For example:

```text
C:\Users\John\Videos\instadl
```

The directory is automatically created if it does not already exist.

This behavior is configured using:

```python
DOWNLOAD_FOLDER = Path.home() / "Videos" / "instadl"
```

This means the Windows username does not need to be hard-coded.

If another Windows user runs InstaDL, the downloader automatically uses that user's `Videos\instadl` directory.

## Download Quality

InstaDL uses the following yt-dlp format selection:

```python
"format": "bestvideo*+bestaudio/best"
```

The downloader therefore attempts to retrieve:

1. The best available video stream
2. The best available audio stream
3. The best combined stream as a fallback

When the highest-quality video and audio are provided as separate streams, FFmpeg merges them into the final MP4 file.

The resulting quality depends on the streams made available by Instagram.

## Global `instadl` Command

InstaDL can be configured as a global Windows command, allowing it to be launched from any directory.

### Create the launcher

Create a file named:

```text
instadl.cmd
```

Add:

```bat
@echo off
py "C:\path\to\instadl\index.py" %*
```

Replace:

```text
C:\path\to\instadl
```

with the actual location where you cloned the repository.

For example:

```bat
@echo off
py "C:\Users\John\Documents\instadl\index.py" %*
```

### Add the launcher to PATH

Add the directory containing `instadl.cmd` to your Windows user `PATH`.

Close and reopen your terminal after changing `PATH`.

You can then run:

```powershell
instadl
```

from any directory.

You can also provide the Instagram URL directly:

```powershell
instadl "https://www.instagram.com/reel/XXXXXXXXXXX/"
```

Regardless of your current terminal directory, downloaded videos are stored in:

```text
C:\Users\<USERNAME>\Videos\instadl
```

## Example

```text
============================================================
Instagram Reel Downloader
============================================================
URL    : https://www.instagram.com/reel/XXXXXXXXXXX/
Folder : C:\Users\John\Videos\instadl

[Instagram] Extracting URL...
[info] Downloading formats...

Downloading: 45.2% | Speed: 5.3MiB/s | ETA: 00:03
Downloading: 100.0% | Speed: 6.1MiB/s | ETA: 00:00

Download finished. Processing video...

============================================================
DOWNLOAD COMPLETE
============================================================
Title    : Example Video
Uploader : example_user
ID       : XXXXXXXXXXX
Quality  : 1080x1920
Folder   : C:\Users\John\Videos\instadl
```

## Updating yt-dlp

Instagram can change how its website and media delivery work over time.

If downloads unexpectedly stop working, update yt-dlp before troubleshooting further:

```powershell
py -m pip install -U yt-dlp
```

If you're using the project's virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
py -m pip install -U yt-dlp
```

## Troubleshooting

### `pip` is not recognized

You don't need to invoke `pip` directly.

Use:

```powershell
py -m pip install -r requirements.txt
```

To verify pip:

```powershell
py -m pip --version
```

### `python` is not recognized

On Windows, try the Python launcher:

```powershell
py --version
```

If Python is installed correctly, you can use `py` throughout the project.

### FFmpeg is not installed

If you receive an error similar to:

```text
ERROR: You have requested merging of multiple formats but ffmpeg is not installed.
```

install FFmpeg:

```powershell
winget install --id Gyan.FFmpeg -e
```

Then close and reopen your terminal.

Verify:

```powershell
ffmpeg -version
```

### Instagram download fails

First update yt-dlp:

```powershell
py -m pip install -U yt-dlp
```

Some Instagram content may require authentication, may be geographically restricted, may have been removed, or may not be accessible through yt-dlp.

Private Instagram content is outside the intended scope of InstaDL.

## Development

The application is intentionally split into small modules to make it easier to maintain and extend.

The current architecture separates:

* CLI handling
* Configuration
* Download logic
* Progress reporting
* URL validation

To run the project during development:

```powershell
py .\index.py
```

Install or update dependencies with:

```powershell
py -m pip install -r requirements.txt
```

## Roadmap

Potential future improvements include:

* [ ] Batch URL downloads
* [ ] Download history
* [ ] Configurable output directories
* [ ] Extended CLI arguments and options
* [ ] Improved logging
* [ ] Automatic dependency checks
* [ ] Automatic FFmpeg detection
* [ ] Duplicate-download detection
* [ ] Unit tests
* [ ] Installable Python package
* [ ] Native `instadl` CLI installation
* [ ] Additional public-video source support

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

If you want to contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

Example:

```bash
git checkout -b feat/my-feature
git commit -m "Add my feature"
git push origin feat/my-feature
```

## Disclaimer

InstaDL is intended for downloading **publicly accessible content that you own or have permission to download**.

Users are responsible for complying with applicable copyright laws, Instagram's terms, and the rights of content owners.

This project is not affiliated with, endorsed by, or sponsored by Instagram or Meta.

## License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

Developed by [Wissem Hammami](https://github.com/WissemHammami009).
