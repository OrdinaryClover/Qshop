##重新定义ORM操作数据库的路由
#核心  重写db_for_read  db_for_write
import random
class Router(object):
    def db_for_read(self,model,**hints):
        ##读数据  使用slave
        return "slave"
        ##设置权重
        # return random.choice(["slave","slave1"])
    def db_for_write(self,model,**hints):
        ##写 使用default
        return "default"
        # return random.choice(["default","master"])
