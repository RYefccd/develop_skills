'''
Created on 2019年8月15日

@author: ryefccd
'''
import pytest
from myproject import mathexample


@pytest.fixture(scope='module')
def resource_a_setup(request):
    print('\nresources_a_setup()')

    def resource_a_teardown():
        print('\nresources_a_teardown()')
    request.addfinalizer(resource_a_teardown)  # 可以在这里回收数据库连接

    return 1234567


def test_add_two(resource_a_setup):
    add = mathexample.add_two(resource_a_setup, 2)
    assert add == 1234567 + 2


def test_sub_two():
    substract = mathexample.sub_two(1, 2)
    assert substract == -1
    print("fccdny")


# @pytest.mark.skip(msg='failure')
def test_add_two_failure():
    add = mathexample.add_two(1, 2)
    assert add == 4


if __name__ == '__main__':
    pass
