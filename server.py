# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import torndb
from config import conf
import redis

from urls import urls
from tornado.options import options, define
from utils.named_dict import Struct, s2d


define("port", default=8000, type=int, help="run server on the given port")
define("conf", default=conf, type=Struct, help="run server on the given port")


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(**s2d(conf.mysql))
        self.redis = redis.StrictRedis(**s2d(conf.redis))


def main():
    options.log_file_prefix = conf.log.log_path
    options.logging = conf.log.log_level

    tornado.options.parse_command_line()
    app = Application(
        urls,
        **s2d(conf.sys),
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()


