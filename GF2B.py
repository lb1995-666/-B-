import os
import time
import shutil

if os.path.exists('BASE_DIR.txt'):
    with open('BASE_DIR.txt', 'r') as f:
        BASE_DIR = f.read()
else:
    BASE_DIR = input("请输入Star Rail根目录: ")
    with open('BASE_DIR.txt', 'w') as f:
        f.write(BASE_DIR)

GAME_DIR = f'{BASE_DIR}\games\Star Rail Game'
PLUGINS_DIR = f'{GAME_DIR}\StarRail_Data\Plugins'
COPY_DIR = 'BFile'


def modify_config():
    # 修改配置config.ini
    with open(f'{GAME_DIR}\config.ini', 'r') as f:
        file_content = f.read()

    file_content_replaced = file_content.replace \
        ('channel=1\nsub_channel=1\ncps=gw_PC', 'channel=14\nsub_channel=0\ncps=bilibili_PC')

    with open(f'{GAME_DIR}\config.ini', 'w') as f:
        f.write(file_content_replaced)
    print('已切换B服配置')


def copy_file():
    file_path1 = f'{COPY_DIR}\sdk_pkg_version'
    fname2 = 'failedlog.db'
    fname3 = 'license.txt'
    fname4 = 'PCGameSDK.dll'

    # 复制文件1
    fpath1 = f'{GAME_DIR}\sdk_pkg_version'
    if os.path.exists(fpath1):
        print(f'{fpath1} 文件已存在')
    else:
        shutil.copyfile(file_path1, fpath1)
        print(f'{fpath1} 文件复制成功')

    # 复制文件2,3,4
    for f in [fname2, fname3, fname4]:
        fpath = PLUGINS_DIR + '\\' + f
        if os.path.exists(fpath):
            print(f'{fpath} 文件已存在')
        else:
            shutil.copyfile(f'{COPY_DIR}\{f}', fpath)
            print(f'{fpath} 文件复制成功')


if __name__ == '__main__':
    modify_config()
    try:
        copy_file()
        print('已切换至B服')
        time.sleep(2)
    except Exception as e:
        print('文件复制报错失败')
        print(e)
        time.sleep(10)
