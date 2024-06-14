# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['N:/python/Sorter/main.py'],
    pathex=[],
    binaries=[],
    datas=[('N:/python/Sorter/Icon.ico', '.')],
    hiddenimports=['_thread', 'win10toast', 'pkg_resources', 'pystray', 'psutil'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Sorter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['G:\\My Drive\\TwinPixel\\Icon\\Normal\\Icon.ico'],
)
