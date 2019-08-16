'''
Created on 2018年8月19日

@author: ryefccd
'''
import json
import asyncio

import aioredis
import tornado.web

from myproject.mathexample import add_two, sub_two
SERVER_REDIS_ADDRESS = ['192.168.1.200', 6379]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        a = int(self.get_argument("a", "6"))
        b = int(self.get_argument("b", "2"))
        num_sum = add_two(a, b)
        num_delta = sub_two(a, b)
        res = {"sum": num_sum,
               "delta": num_delta,
               "a": a,
               "b": b}
        self.write(json.dumps(res))

application = tornado.web.Application([
    (r"/", MainHandler),
])


def init_app(ioloop, application):
    redis_conn = std_loop.run_until_complete(
        aioredis.create_redis_pool(SERVER_REDIS_ADDRESS, db=0))
    application.settings["REDIS_CONN"] = redis_conn


if __name__ == '__main__':
    std_loop = asyncio.get_event_loop()
    init_app(std_loop, application)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8989)
    std_loop.run_forever()
