# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller recipe for a portable StockWatch executable."""

from pathlib import Path

project = Path(SPECPATH)

a = Analysis(
    [str(project / "server.py")],
    pathex=[str(project)],
    binaries=[],
    datas=[(str(project / "web"), "web")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="StockWatch",
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
