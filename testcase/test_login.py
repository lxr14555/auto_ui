import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from common.log import log
from common.selenuim_po import sel_click, sel_send_keys, get_text
from common.sql import MysqlAuto
from po import event
from po.event import Event
from settings import ENV


class TestLogin:


    @pytest.mark.parametrize(("username", "password", "result"), [
        ('test1', 'test1', '欢迎您：test1 | 退出'),
        ('name', 'test1', '用户名错误'),
        ('test1', 'pass', '密码错误')], ids=
        ('test_shopping_mall_01', 'test_shopping_mall_02', 'test_shopping_mall_03')
    )
    # def test_shopping_mall_01(self, username, password, result):
    def test_shopping_mall(self, username, password, result, login):
        # self.driver = webdriver.Chrome()
        # self. driver.get("http://127.0.0.1:8000/")
        # self. driver.maximize_window()
        # self. driver.implicitly_wait(10)
        # sleep(3)
        driver = login
        driver.get(ENV.url)
        # driver.find_element(By.XPATH, "//a[contains(text(),'登录')]").click()
        sel_click(driver, (By.XPATH, "//a[contains(text(),'登录')]"))
        sleep(1)
        # driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名']").send_keys(username)
        sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入用户名']"), username)
        sleep(1)
        # driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']").send_keys(password)
        sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入密码']"), password)
        sleep(1)
        # driver.find_element(By.XPATH, "//input[@value='登录']").click()
        sel_click(driver, (By.XPATH, "//input[@value='登录']"))
        sleep(1)

        if '欢迎您' in result:
            text = driver.find_element(By.XPATH, "//div[@class='login_btn fl']").text
            assert text == result

            driver.find_element(By.XPATH, "//a[contains(text(),'退出')]").click()
        elif '用户名错误' in result:
            text = driver.find_element(By.XPATH, "//div[@class='user_error']").text
            assert text == result
        elif '密码错误' in result:
            text = driver.find_element(By.XPATH, "//div[@class='pwd_error']").text
            assert text == result

    def test_shopping_mall_04(self, open_page):
        username = 'test123'
        password = 'test123'
        cpwd = 'test123'
        email = 'test123@qq.com'
        driver = open_page
        sel_click(driver, (By.XPATH, "//a[contains(text(),'注册')]"))
        # sleep(1)
        sel_send_keys(driver, (By.XPATH, "//input[@id='user_name']"), username)
        sel_send_keys(driver, (By.XPATH, "//input[@id='pwd']"), password)
        sel_send_keys(driver, (By.XPATH, "//input[@id='cpwd']"), cpwd)
        sel_send_keys(driver, (By.XPATH, "//input[@id='email']"), email)
        sel_click(driver, (By.XPATH, "//input[@value='注 册']"))
        sleep(2)
        # 断言1 查询用户表，检验该用户是否存在
        sql = [f'select * from df_user_userinfo where uname = "{username}"']
        result = MysqlAuto().execute(sql)
        assert username in result[0]

        #断言2 检查注册用户是否登录正常
        Event().event_login(driver, username, password)
        text = driver.find_element(By.XPATH, "//div[@class='login_btn fl']").text
        assert text == f'欢迎您：{username} | 退出'
        sleep(3)



