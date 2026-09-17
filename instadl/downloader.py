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


def build_ydl_options() -> dict:

    return {

        # Quality
        "format": VIDEO_FORMAT,

        # Merge
        "merge_output_format": MERGE_FORMAT,

        # Output
        "paths": {
            "home": str(DOWNLOAD_FOLDER),
        },

        "outtmpl": OUTPUT_TEMPLATE,

        # Download
        "noplaylist": True,

        "concurrent_fragment_downloads":
            CONCURRENT_FRAGMENTS,

        "retries": RETRIES,

        "fragment_retries":
            FRAGMENT_RETRIES,

        # Progress
        "progress_hooks": [
            progress_hook
        ],
    }


def download_instagram_reel(url: str):

    DOWNLOAD_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    print("=" * 60)
    print("Instagram Reel Downloader")
    print("=" * 60)

    print(f"URL    : {url}")
    print(f"Folder : {DOWNLOAD_FOLDER}")

    print()

    try:

        ydl_opts = build_ydl_options()

        with yt_dlp.YoutubeDL(
            ydl_opts
        ) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            print_download_info(info)

    except yt_dlp.utils.DownloadError as error:

        print()
        print("Download failed:")
        print(error)

    except Exception as error:

        print()
        print("Unexpected error:")
        print(error)


def print_download_info(info: dict):

    print()
    print("=" * 60)
    print("DOWNLOAD COMPLETE")
    print("=" * 60)

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

    width = info.get("width")
    height = info.get("height")

    if width and height:

        print(
            f"Quality  : "
            f"{width}x{height}"
        )

    print(
        f"Folder   : "
        f"{DOWNLOAD_FOLDER}"
    )