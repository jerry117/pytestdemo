#coding:utf-8

import time

# 命令行运行命令
# pytest -v -s --durations=3 test_some_are_slow.py
# 统计用例运行时间

def test_funcfast():
    time.sleep(0.1)

def test_funcslow1():
    time.sleep(0.2)

def test_funcslow2():
    time.sleep(0.3)

