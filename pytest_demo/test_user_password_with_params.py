#coding:utf-8


import pytest
import json
users = json.loads(open('./users.dev.json', 'r').read())

# 参数化示例方法二（单个参数）
class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param


    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has a weak password" % (user['name'])
        assert passwd != 'password', msg
        assert passwd != 'password123', msg
