#coding:utf-8

import requests
import pytest

class TestV2exApi(object):
    domain = "https://www.v2ex.com/"

    def test_node(self):
        path = "api/nodes/show.json?name=python"
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == 'python'
        assert res['id'] == 90

# 参数化接口请求
class TestV2exApiWithParams(object):
    domain = "https://www.v2ex.com/"


    @pytest.fixture(params=['python', 'java', 'go', 'nodejs'])
    def lang(self, request):
        # 每次都可以用request.param来访问本次传入fixture中的参数
        return request.param

    # 在测试方法中传入同名的fixture方法名可以直接访问fixture
    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' % (lang)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == lang
        # 强制用例失败，看fixture的参数值
        # assert 0

# 使用fixture参数化测试预期结果
class TestV2exApiWithExpectation(object):
    domain = 'https://www.v2ex.com/'

    @pytest.mark.parametrize('name,node_id', [('python', 90), ('java', 63), ('go', 375), ('nodejs', 436)])

    def test_node(self, name, node_id):
        path = 'api/nodes/show.json?name=%s' %(name)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == name
        assert res['id'] == node_id
        # assert 0
