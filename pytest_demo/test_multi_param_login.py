import pytest

test_user_data1 = [
    {'user':'jerry', 'password': '123456'},
    {'user':'tom', 'password': '654321'},
    {'user':'test1', 'password': ''},
]

test_user_data2 = [
    {'q':'中国平安', 'count': 3, 'page':1},
    {'q':'阿里巴巴', 'count': 2, 'page':2},
    {'q':'pdd', 'count': 3, 'page':1},
]

@pytest.fixture(scope='module')
def login_r(request):
    user = request.param['user']
    pwd = request.param['password']
    print('用户登录名{}用户登录密码{}'.format(user, pwd))

@pytest.fixture(scope='module')
def query_param(request):
    q = request.param['q']
    count = request.param['count']
    page = request.param['page']
    print('搜索关键词{}'.format(q))
    return request.param

@pytest.mark.parametrize('query_param', test_user_data2, indirect=True)
@pytest.mark.parametrize('login_r', test_user_data1, indirect=True)
def test_login(login_r, query_param):
    a = login_r
    print('登录后的返回值{}'.format(a))
    b = query_param
    print('接口查询返回{}'.format(b))

    
