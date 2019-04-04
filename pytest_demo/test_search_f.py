import os
import yaml
import pytest
import requests

def _base_data(file_name):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # print(cur_path)
    yaml1 = os.path.join(cur_path, file_name)
    f1 = open(yaml1) #打开yaml文件
    data = yaml.load(f1) #使用load方法加载
    return data  

@pytest.fixture(autouse=True, scope='module')
def get_base_data():
    base_data = _base_data('test_search.yml')
    for v in base_data.values():
        return v


# @pytest.fixture(autouse=True)   #如果数据只有一条要放开这个装饰器
def get_test_data():
    test_data = _base_data('test_search_data.yml')
    payload = test_data.get('payload')
    # payload = test_data.values()
    return payload

@pytest.fixture(autouse=True)
def query_param(request):
    return request.param

@pytest.mark.parametrize('query_param', get_test_data(), indirect=True)   #如果数据只有一条要注释这个装饰器
def test_search(get_base_data, query_param):
    method = get_base_data.get('method')
    url = get_base_data.get('url')
    headers = get_base_data.get('header')
    param = query_param
    res = requests.request(method=method, url=url, headers=headers, params=param)
    print(res.text)

