import app
import logging
# 初始化日志
# 为什么要在api.__init__.py中初始化日志呢？
# 这是因为我们后面进行接口测试，都会条用封装的API接口调用时自动运行—__init—__.py
# 从而实现，自动化初始化日志的功能
app.init__logging()

logging.info("TEST日志器能不能正常工作")
