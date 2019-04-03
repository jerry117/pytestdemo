#coding:utf-8

from pytest_demo import login_test
import pytest

def zero_error():
    return 1/1


# 判断函数抛出的异常是否正确
def test_zero_division():
    with pytest.raises(ZeroDivisionError, message="定制断言异常的错误信息"):
        # do_something
        zero_error()

# 访问异常的具体信息
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        print(excinfo)
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)