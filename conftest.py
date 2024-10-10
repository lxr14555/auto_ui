import pytest
from selenium import webdriver

from common.log import log
from setting import ENV


@pytest.fixture(scope='class')
def login():
    driver = webdriver.Chrome()
    driver.get(ENV.url)
    log.debug('打开浏览器')
    driver.maximize_window()
    log.debug('最大化窗口')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    log.debug('浏览器关闭')