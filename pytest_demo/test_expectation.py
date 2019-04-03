#coding:utf-8

import pytest

# parametrize多个参数传入。

@pytest.mark.parametrize("test_input, expected",[
    ("3+5", 8),("2+4", 6),("6*9", 45)
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected