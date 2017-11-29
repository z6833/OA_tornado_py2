# coding=utf-8
from dbsession import engine
from dbsession import Base

#将创建好的model中的类，映射到数据库中
def run():
    print "---create_all----"
    Base.metadata.create_all(engine)
    print "---create_end----"

if __name__ == "__main__":
    run()
