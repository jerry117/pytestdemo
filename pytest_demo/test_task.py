from collections import namedtuple
import pytest
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    print(t1)
    assert t1 == t2


def test_member_access():
    t = Task('buy milk', 'brian')
    pytest.assume(t.summary == 'buy milk1')
    print('run two case')
    pytest.assume(t.owner == 'brian')
    pytest.assume((t.done, t.id) == (False, None))
