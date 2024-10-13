import pytest
from selenium import webdriver

from common.log import log
from common.sql import MysqlAuto
from po.event import Event
from po.home_page import HomePage
from settings import ENV, DBSql


@pytest.fixture(scope='class')
def login():
    global driver
    driver = HomePage()
    Event.event_login(driver, ENV.user_name, ENV.pass_word)
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def open_page():
    driver = webdriver.Chrome()
    driver.get(ENV.url)
    log.debug('打开浏览器')
    driver.maximize_window()
    log.debug('最大化窗口')
    driver.implicitly_wait(10)
    # 初始化数据
    # MysqlAuto().execute(DBSql.sql_list)
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def open_homepage():
    # 定义一个全局变量
    global driver
    # 初始化HomePage实例
    driver = HomePage()
    # 打开首页
    driver.get(ENV.url)
    # 把driver返回，传过去
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest 失败后执行
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    out = yield
    result = out.get_result()
    log.info(f"test report:{result}")
    log.info(f"execution time-consuming:{round(call.duration, 2)} second")
    # if result.failed and result.when == 'call':
    if result.failed:
        try:
            log.info('error.screenshot.')
            driver.allure_save_screenshot('error_screenshot')
        except Exception as e:
            log.error(e)
            pass
