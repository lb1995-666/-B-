import os
import time

if os.path.exists('BASE_DIR.txt'):
    with open('BASE_DIR.txt', 'r') as f:
        BASE_DIR = f.read()
else:
    BASE_DIR = input("请输入Star Rail根目录: ")
    with open('BASE_DIR.txt', 'w') as f:
        f.write(BASE_DIR)

GAME_DIR = f'{BASE_DIR}\games\Star Rail Game'
PLUGINS_DIR = f'{GAME_DIR}\StarRail_Data\Plugins'


def modify_config():
    # 修改配置config.ini
    with open(f'{GAME_DIR}\config.ini', 'r') as f:
        file_content = f.read()

    file_content_replaced = file_content.replace\
        ('channel=14\nsub_channel=0\ncps=bilibili_PC', 'channel=1\nsub_channel=1\ncps=gw_PC')

    with open(f'{GAME_DIR}\config.ini', 'w') as f:
        f.write(file_content_replaced)
    print('已切换国服配置')


def delete_file():
    # 删除B服4个文件
    file_path1 = f'{GAME_DIR}\sdk_pkg_version'
    file_path2 = f'{PLUGINS_DIR}\\failedlog.db'
    file_path3 = f'{PLUGINS_DIR}\license.txt'
    file_path4 = f'{PLUGINS_DIR}\PCGameSDK.dll'

    for fpath in [file_path1, file_path2, file_path3, file_path4]:
        if os.path.exists(fpath):
            os.remove(fpath)
            print(f'{fpath} 文件已删除')
        else:
            print(f'{fpath} 文件不存在')


if __name__ == '__main__':
    modify_config()
    delete_file()
    print('已切换到国服')
    time.sleep(2)
