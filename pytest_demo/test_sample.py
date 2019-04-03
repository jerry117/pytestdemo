#coding:utf-8
import pytest
import allure

# login_test.py # 登录相关功能的测试用例
# cart_test.py # 购物车相关功能的测试用例
# checkout_test.py # 结算相关功能的用例
# order_test.py # 订单相关功能的用例

def inc(x):
    return x+1

def test_answer():
    assert inc(3) == 5

def test_needs(tmpdir):
    print(tmpdir)
    assert 0

if __name__ == '__main__':
#     pytest.main(r"C:\Users\Administrator\PycharmProjects\untitled\pytest_demo")
    pytest.main()