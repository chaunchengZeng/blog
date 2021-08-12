# coding=utf-8
"""
author: zcc
time: 2021/8/12 9:01
file: main.py
"""
import re
import time
import subprocess
from random import randint
import url


class Base(object):

    @staticmethod
    def grep(file):
        """
        根据html文本匹配出url链接
        :param file:
        :return:
        """
        with open(file, 'r', encoding='utf-8', ) as f:
            html = f.read()
        _url = re.findall(r'https://blog.csdn.net/chuancheng_zeng/article/details/\d{9}', html)
        print(len(_url))
        print(_url)

        for i in _url:
            if i not in url.url:
                url.url.append(i)

        with open(r'./blog/url.txt', 'w', encoding='utf-8', ) as f:
            f.write('\n'.join(url.url))

    @staticmethod
    def curl(_url):
        for u in _url:
            try:
                subprocess.check_output(f'curl -s {u}', shell=True)
                # print("print ", res.decode('utf-8'))
            except subprocess.CalledProcessError as e:
                print(e.output)
                print(e.returncode)


if __name__ == '__main__':
    a = Base()
    for i in range(1000):
        print(f"第{i+1}轮")
        a.curl(url.url)
        seconds = randint(30, 70)
        time.sleep(seconds)
