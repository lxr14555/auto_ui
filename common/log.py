
import logging
import os
import time

import colorlog

from config.conf import BASE_DIR


log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

log = logging.getLogger('log_name')

# 输出到控制台
console_handler = logging.StreamHandler()
daytime = time.strftime('%Y-%m-%d')  # %Y-%m-%d_%H-%M-%S
path = BASE_DIR + '/log/'
if not os.path.exists(path):
    os.makedirs(path)
filename = path + f'/run_log_{daytime}.log'
# 输出到文件
file_handler = logging.FileHandler(filename=filename, mode='a', encoding='utf8')

# 日志级别，log 和 handler以最高级别为准，不同handler之间可以不一样，不相互影响
log.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# 日志输出格式
file_formatter = logging.Formatter(
    # fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    fmt='[%(levelname)s] [%(asctime)s.%(msecs)03d] : %(message)s %(filename)s -> %(funcName)s line:%(lineno)d ',
    datefmt='%Y-%m-%d  %H:%M:%S'
)
console_formatter = colorlog.ColoredFormatter(
    # fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    fmt='[%(levelname)s] %(log_color)s[%(asctime)s.%(msecs)03d] : %(message)s %(filename)s -> %(funcName)s line:%(lineno)d ',
    datefmt='%Y-%m-%d  %H:%M:%S',
    log_colors=log_colors_config
)
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# 重复日志问题：
# 1、防止多次addHandler；
# 2、logname 保证每次添加的时候不一样；
# 3、显示完log之后调用removeHandler
if not log.handlers:
    log.addHandler(console_handler)
    log.addHandler(file_handler)

console_handler.close()
file_handler.close()

if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
