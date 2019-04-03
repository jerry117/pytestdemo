#coding:utf-8

import pytest
import json
# 测试数据参数化demo（单个参数）
class TestUserPassword(object):
    # 获取用户账号密码文件
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json', 'r').read())

    def test_user_password(self, users):
        for user in users:
            passwd = user['password']
            # 三个assert是递进关系，重要的放前面，换句话说任何1个assert失败后，用例就终止运行了
            assert len(passwd)>=6
            msg = "user {} has a weak password".format(user['name'])
            assert passwd != 'password', msg
            assert passwd != 'password123', msg

