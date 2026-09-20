from pathlib import Path

import yt_dlp

from instadl.config import (
    DOWNLOAD_FOLDER,
    VIDEO_FORMAT,
    MERGE_FORMAT,
    OUTPUT_TEMPLATE,
    CONCURRENT_FRAGMENTS,
    RETRIES,
    FRAGMENT_RETRIES,
)

from instadl.progress import progress_hook
from instadl.runtime import (
    get_ffmpeg_path,
    get_ffprobe_path,
)


# ============================================================
# YT-DLP CONFIGURATION
# ============================================================

def build_ydl_options() -> dict:

    ffmpeg_path = get_ffmpeg_path()
    ffprobe_path = get_ffprobe_path()

    # --------------------------------------------------------
    # Verify bundled FFmpeg binaries
    # --------------------------------------------------------

    if not ffmpeg_path.exists():
        raise FileNotFoundError(
            f"FFmpeg was not found at: {ffmpeg_path}"
        )

    if not ffprobe_path.exists():
        raise FileNotFoundError(
            f"FFprobe was not found at: {ffprobe_path}"
        )

    # yt-dlp accepts the directory containing ffmpeg/ffprobe.
    ffmpeg_directory = ffmpeg_path.parent

    return {

        # ----------------------------------------------------
        # Quality
        # ----------------------------------------------------

        "format": VIDEO_FORMAT,

        # ----------------------------------------------------
        # FFmpeg
        # ----------------------------------------------------

        "ffmpeg_location": str(ffmpeg_directory),

        "merge_output_format": MERGE_FORMAT,

        # ----------------------------------------------------
        # Output
        # ----------------------------------------------------

        "paths": {
            "home": str(DOWNLOAD_FOLDER),
        },

        "outtmpl": OUTPUT_TEMPLATE,

        # ----------------------------------------------------
        # Download
        # ----------------------------------------------------

        "noplaylist": True,

        "concurrent_fragment_downloads":
            CONCURRENT_FRAGMENTS,

        "retries":
            RETRIES,

        "fragment_retries":
            FRAGMENT_RETRIES,

        # ----------------------------------------------------
        # Progress
        # ----------------------------------------------------

        "progress_hooks": [
            progress_hook
        ],

        # ----------------------------------------------------
        # General
        # ----------------------------------------------------

        "quiet": False,
        "no_warnings": False,
    }


# ============================================================
# DOWNLOAD
# ============================================================

def download_instagram_reel(url: str):

    # --------------------------------------------------------
    # Create download directory
    # --------------------------------------------------------

    DOWNLOAD_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    print("=" * 60)
    print("InstaDL")
    print("=" * 60)

    print(f"URL    : {url}")
    print(f"Folder : {DOWNLOAD_FOLDER}")

    print()

    try:

        # ----------------------------------------------------
        # Build yt-dlp configuration
        # ----------------------------------------------------

        ydl_opts = build_ydl_options()

        # ----------------------------------------------------
        # Start download
        # ----------------------------------------------------

        with yt_dlp.YoutubeDL(
            ydl_opts
        ) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

        # ----------------------------------------------------
        # Display result
        # ----------------------------------------------------

        print_download_info(info)

    except FileNotFoundError as error:

        print()
        print("=" * 60)
        print("DEPENDENCY ERROR")
        print("=" * 60)

        print(error)

        print()
        print(
            "The required FFmpeg binaries "
            "could not be found."
        )

    except yt_dlp.utils.DownloadError as error:

        print()
        print("=" * 60)
        print("DOWNLOAD FAILED")
        print("=" * 60)

        print(error)

    except KeyboardInterrupt:

        print()
        print()
        print("Download cancelled by user.")

    except Exception as error:

        print()
        print("=" * 60)
        print("UNEXPECTED ERROR")
        print("=" * 60)

        print(error)


# ============================================================
# DOWNLOAD INFORMATION
# ============================================================

def print_download_info(info: dict):

    print()
    print("=" * 60)
    print("DOWNLOAD COMPLETE")
    print("=" * 60)

    # --------------------------------------------------------
    # Metadata
    # --------------------------------------------------------

    print(
        f"Title    : "
        f"{info.get('title', 'Unknown')}"
    )

    print(
        f"Uploader : "
        f"{info.get('uploader', 'Unknown')}"
    )

    print(
        f"ID       : "
        f"{info.get('id', 'Unknown')}"
    )

    # --------------------------------------------------------
    # Resolution
    # --------------------------------------------------------

    width = info.get("width")
    height = info.get("height")

    if width and height:

        print(
            f"Quality  : "
            f"{width}x{height}"
        )

    # --------------------------------------------------------
    # Output directory
    # --------------------------------------------------------

    print(
        f"Folder   : "
        f"{DOWNLOAD_FOLDER}"
    )