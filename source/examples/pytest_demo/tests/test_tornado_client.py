'''
Created on 2019年8月15日

@author: ryefccd
'''
import json
import pytest
from myproject import handler


@pytest.fixture
def app():
    return handler.application


@pytest.fixture(scope="function")
def db_init(io_loop, app):
    std_ioloop = io_loop.asyncio_loop
    handler.init_app(io_loop, app)
    # 填充数据库数据
    yield
    # 清楚数据库数据
    conn = app.settings["REDIS_CONN"]
    conn.close()
    std_ioloop.run_until_complete(conn.wait_closed())


@pytest.mark.gen_test
def test_tornao_request_success(http_client, base_url):
    url = base_url + "?a=7&b=2"
    print("url:", url)
    print("base_url:", base_url)
    print("http_client:", http_client)
    response = yield from http_client.fetch(url)

    assert response.code == 200


@pytest.mark.gen_test
def test_tornao_request_fail(http_client, base_url):
    url = base_url + "?a=7&b=2"
    print("url:", url)
    print("base_url:", base_url)
    print("http_client:", http_client)
    response = yield from http_client.fetch(url)
    res = json.loads(response.body.decode())
    print(res)
    assert response.code == 200
    assert res["sum"] == 10


if __name__ == '__main__':
    pass
