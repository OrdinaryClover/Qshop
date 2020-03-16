import logging

##进行日志的配置  日志的等级
format = "%(asctime)s【%(levelname)s】%(message)s"


datefmt = "%Y-%m-%d %H:%M:%S"
##收集日志  将日志写入到文件中
file_handlers = logging.FileHandler("test.log",encoding="utf-8")
##控制台输出日志
stream_handlers = logging.StreamHandler()

logging.basicConfig(level=logging.DEBUG,format=format,datefmt=datefmt,handlers=[file_handlers,stream_handlers])


""" 
level要收集的日志等级  默认是warning
format  可以定义输出的日志的格式
datefmt  时间格式
"""

logging.debug("我是debug")
logging.info("我是info")
logging.warning("我是warning")
logging.error("我是error")
logging.critical("我是crticle")