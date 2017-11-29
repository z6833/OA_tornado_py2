# coding=utf-8
import tornado.escape
from libs.pycket.session import SessionMixin
from libs.db.dbsession import dbSession
from libs.redis_conn.redis_conn import conn
from models.accounts.account_user_model import User

users = {
    'user':User
}
class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def initialize(self):
        self.db = dbSession
        self.conn = conn

    def get_current_user(self):
        '''获取当前用户'''
        # username = self.session.get("user_name")
        # if username:
        #     user = users[]
        return None

    def on_finish(self):
        self.db.close()

