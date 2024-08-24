# coding=utf-8

import requests
import os

check_new_version_url = 'https://byfuns.github.io/zh-cn/wymusic/version.txt'




headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; V2302A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 VivoBrowser/21.0.60.0'}

# 创建安装文件夹
if not os.path.exists('MD'):
    os.mkdir('MD')

# 获取最新版本
version = requests.get(url=check_new_version_url, headers=headers).text.strip().split('\n')[-1]

# 下载最新版本
downlaod_new_version_url = f'https://byfuns.github.io/zh-cn/wymusic/{version}/main.py'
r = requests.get(url=downlaod_new_version_url, headers=headers)
with open('MD/main.py', 'wb') as fp:
    fp.write(r.content)
print('下载完成。你的下载命令为：\n\ncd ~ && cd MD && python main.py\n\n')
