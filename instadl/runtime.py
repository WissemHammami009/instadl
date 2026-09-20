import sys
from pathlib import Path


def get_bundle_dir() -> Path:
    """
    Return the directory containing bundled application resources.

    Development:
        <project root>

    PyInstaller:
        temporary/internal bundle directory
    """

    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)

    return Path(__file__).resolve().parent.parent


def get_ffmpeg_path() -> Path:
    return get_bundle_dir() / "bin" / "ffmpeg.exe"


def get_ffprobe_path() -> Path:
    return get_bundle_dir() / "bin" / "ffprobe.exe"