import logging
import shutil
import time
import os

# 系统日志格式
console_fmt = "[%(asctime)s]-[%(levelname)s]-[%(filename)s] : %(message)s"
systemlog_path = 'log\SystemLog'

class Logger:

    def __init__(self, name=None):
        self.check_file()
        self.name = name
        # ①创建一个记录器
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel("INFO")  # 设置日志级别为 'level'，即只有日志级别大于等于'level'的日志才会输出
        self.formatter = logging.Formatter(console_fmt)  # 创建formatter
        # ②创建屏幕-输出到控制台，设置输出等级
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setLevel("DEBUG")
        # ③创建log文件，设置输出等级
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 根目录
        log_path = os.path.join(PROJECT_ROOT, systemlog_path)
        time_now = time.strftime('%Y_%m%d', time.localtime()) + '.log'  # log文件命名：2022_0402.log
        self.fileHandler = logging.FileHandler(os.path.join(log_path, time_now), 'a', encoding='utf-8')
        self.fileHandler.setLevel("DEBUG")
        # ④用formatter渲染这两个Handler
        self.streamHandler.setFormatter(self.formatter)
        self.fileHandler.setFormatter(self.formatter)
        # ⑤将这两个Handler加入logger内
        self.logger.addHandler(self.streamHandler)
        self.logger.addHandler(self.fileHandler)

    def getLogger(self):
        return self.logger

    def check_file(self):
        parent_dir = os.getcwd()
        print(os.path.join(parent_dir, systemlog_path))
        # 检查项目目录是否存在systemlog文件夹
        if os.path.isdir(os.path.join(parent_dir, systemlog_path)):
            pass
        else:
            # 创建systemlog文件夹
            os.mkdir(os.path.join(parent_dir, systemlog_path))
            print('已创建%s文件夹' % systemlog_path)


if __name__ == '__main__':
    logger = Logger().getLogger()
    logger.info('测试')
