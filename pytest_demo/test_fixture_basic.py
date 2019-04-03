#coding:utf-8

import pytest

# 运行命令
# -s 显示方法里面的print
# pytest -v  -s test_fixture_basic.py

# 先定义运行前每个case的方法
@pytest.fixture()
def before():
    print ('\nbefore each test')

def test_1(before):
    print ('test_1()')

def test_2(before):
    print ('test_2()')
    assert 0

# case运行前先执行before方法
@pytest.mark.usefixtures("before")
def test_3():
    print('test_3()')

@pytest.mark.usefixtures("before")
class Test2:
    def test_5(self):
        print('test_5()')

    def test_6(self):
        print('test_6()')

class Test1:
    @pytest.mark.usefixtures("before")
    def test_4(self):
        print('test_4()')

