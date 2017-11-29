#coding=utf-8
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from config import settings
from handlers.main.main_urls import handlers
#定义一个默认的端口
define("port", default=8000, help="run port ", type=int)
define("start", default=False, help="start server", type=bool)


if __name__ == "__main__":
    options.parse_command_line()
    if options.start:
        app = tornado.web.Application(handlers, **settings) #创建应用实例
        http_server = tornado.httpserver.HTTPServer(app) #通过应用实例创建服务器实例
        http_server.listen(options.port)  #监听8000端口
        print 'start server...'
        tornado.ioloop.IOLoop.instance().start() #启动服务器

