import pytest

test_user_data = [
    {'user':'jerry', 'password': '123456'},
    {'user':'tom', 'password': '654321'},
    {'user':'test1', 'password': ''},
]

@pytest.fixture(scope='module')
def login_r(request):
    user = request.param['user']
    pwd = request.param['password']
    print('用户登录名{}用户登录密码{}'.format(user, pwd))
    if pwd:
        return True
    else:
        return False

@pytest.mark.parametrize('login_r', test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print('登录后的返回值{}'.format(a))
    assert a, '失败原因密码为空'






