# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['alien_invasion.py'],
             pathex=['alien.py', 'bullet.py', 'button.py', 'game_function.py', 'game_stats.py', 'scoreboard.py', 'setting.py', 'ship.py', 'D:\\python\\alion'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='alien_invasion',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='alien_invasion')
