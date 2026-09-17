from pathlib import Path


# ============================================================
# DOWNLOAD
# ============================================================

DOWNLOAD_FOLDER = Path.home() / "Videos" / "instadl"


# ============================================================
# YT-DLP
# ============================================================

VIDEO_FORMAT = "bestvideo*+bestaudio/best"

MERGE_FORMAT = "mp4"

OUTPUT_TEMPLATE = "%(uploader)s - %(id)s.%(ext)s"

CONCURRENT_FRAGMENTS = 4

RETRIES = 10

FRAGMENT_RETRIES = 10