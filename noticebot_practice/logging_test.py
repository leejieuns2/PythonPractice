import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

# 현재 시간 Log 출력을 위한 변수
now = datetime.now()

# format : default format customizing
# datefmt : customizing asctime format
# filename : setting file name
# level : min level to print log
logging.basicConfig(format='(%(asctime)s) : %(levelname)s : %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S',
                    filename='./noticebot_practice/example.log',
                    level=logging.DEBUG)

# botLogger = logging.getLogger()
# rotatingHandler = logging.handlers.TimedRotatingFileHandler(
#     filename='./noticebot_practice/example.log', when='midnight', interval=1, encoding='utf-8')
# botLogger.addHandler(rotatingHandler)

logging.critical('critical logging')    # value 50
logging.error('error logging')          # value 40
logging.warning('warning logging')      # value 30
logging.info('info logging')            # value 20
logging.debug('debug logging')          # value 10
