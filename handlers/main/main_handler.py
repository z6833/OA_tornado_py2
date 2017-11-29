# coding=utf-8

import tornado.web

from handlers.base.base_handler import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html")
