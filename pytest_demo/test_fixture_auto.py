#coding:utf-8

import time
import pytest

# fixture scope
# function：每个test都运行，默认是function的scope
# class：每个class的所有test只运行一次
# module：每个module的所有test只运行一次   module代表一个py文件
# session：每个session只运行一次


# module在该module内运行了一次，
@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module : %s'% request.module.__name__)
    print('-------------------')


# func_header对每个test都运行了一次。
@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n-----------------')
    print('function : %s'% request.function.__name__)
    print('time     : %s '%time.asctime())
    print('-------------------')


def test_one():
    print('in test_one()')

def test_two():
    print('in test_two()')
