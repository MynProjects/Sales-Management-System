# -*- mode: python -*-

block_cipher = None


a = Analysis(['sms_startup_script.py',
              'all_items.py',
              'all_items_ui.py',
              'all_sales_persons.py',
              'all_sales_persons_ui.py',
              'daily_graph_window.py',
              'daily_graph_window_ui.py',
              'display_graph.py',
              'display_graph_ui.py',
              'login.py',
              'login_ui.py',
              'login_records.py',
              'login_records_ui.py',
              'monthly_graph_window.py',
              'monthly_graph_window_ui.py',
              'msg_template.py',
              'msg_template_ui.py',
              'sms_main.py',
              'sms_main_ui.py',
              'startup_login_setup.py',
              'startup_login_setup_ui.py',
              'threaded_functions.py',
              'yearly_graph_window.py',
              'yearly_graph_window_ui.py'],
             pathex=['C:\\Users\\ROSAR\\Desktop\\Sales Management System'],
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

a.datas += Tree('./data_files', prefix='data_files')
a.datas += Tree('./dbs', prefix='dbs')
a.datas += Tree('./icons', prefix='icons')
a.datas += Tree('./notifications', prefix='notifications')
a.datas += Tree('./search_history', prefix='search_history')

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='sms',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='.\\icons\\sms_icon64x64.ico' )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='SMS', icon='.\\icons\\sms_icon64x64.ico')
