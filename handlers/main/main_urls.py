# coding=utf-8

from tornado.web import StaticFileHandler
from main_handler import MainHandler

handlers = [
    (r'/', MainHandler),
]