# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import collect_all


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(SPECPATH)

APP_NAME = "InstaDL"

ENTRY_POINT = PROJECT_ROOT / "index.py"

ICON_FILE = PROJECT_ROOT / "assets" / "instadl.ico"

FFMPEG_FILE = PROJECT_ROOT / "bin" / "ffmpeg.exe"

FFPROBE_FILE = PROJECT_ROOT / "bin" / "ffprobe.exe"


# ============================================================
# VALIDATION
# ============================================================

if not ICON_FILE.exists():
    raise FileNotFoundError(
        f"Application icon not found: {ICON_FILE}"
    )

if not FFMPEG_FILE.exists():
    raise FileNotFoundError(
        f"FFmpeg not found: {FFMPEG_FILE}"
    )

if not FFPROBE_FILE.exists():
    raise FileNotFoundError(
        f"FFprobe not found: {FFPROBE_FILE}"
    )


# ============================================================
# YT-DLP
# ============================================================

yt_dlp_datas, yt_dlp_binaries, yt_dlp_hiddenimports = collect_all(
    "yt_dlp"
)


# ============================================================
# ANALYSIS
# ============================================================

a = Analysis(

    [
        str(ENTRY_POINT)
    ],

    pathex=[
        str(PROJECT_ROOT)
    ],

    binaries=[

        (
            str(FFMPEG_FILE),
            "bin"
        ),

        (
            str(FFPROBE_FILE),
            "bin"
        ),

        *yt_dlp_binaries,
    ],

    datas=[
        *yt_dlp_datas,
    ],

    hiddenimports=[
        *yt_dlp_hiddenimports,
    ],

    hookspath=[],

    hooksconfig={},

    runtime_hooks=[],

    excludes=[],

    noarchive=False,

    optimize=0,
)


# ============================================================
# PYZ
# ============================================================

pyz = PYZ(
    a.pure
)


# ============================================================
# EXE
# ============================================================

exe = EXE(

    pyz,

    a.scripts,

    [],

    exclude_binaries=True,

    name=APP_NAME,

    # --------------------------------------------------------
    # Windows application icon
    # --------------------------------------------------------

    icon=str(ICON_FILE),

    # --------------------------------------------------------
    # Configuration
    # --------------------------------------------------------

    debug=False,

    bootloader_ignore_signals=False,

    strip=False,

    upx=True,

    console=True,

    disable_windowed_traceback=False,

    argv_emulation=False,

    target_arch=None,

    codesign_identity=None,

    entitlements_file=None,
)


# ============================================================
# COLLECT
# ============================================================

coll = COLLECT(

    exe,

    a.binaries,

    a.datas,

    strip=False,

    upx=True,

    upx_exclude=[],

    name=APP_NAME,
)