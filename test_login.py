import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


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

        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'登录')]").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名']").send_keys(username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名']").send_keys(username)
        sleep(1)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']").send_keys(password)
        sleep(1)
        self.driver.find_element(By.XPATH, "//input[@value='登录']").click()
        sleep(1)
        if '欢迎您' in result:
            text = self.driver.find_element(By.XPATH, "//div[@class='login_btn fl']").text
            # assert text == result
            assert text == result
            self.driver.find_element(By.XPATH, "//a[contains(text(),'退出')]").click()
        elif '用户名错误' in result:
            text = self.driver.find_element(By.XPATH, "//div[@class='user_error']").text
            assert text == result
        elif '密码错误' in result:
            text = self.driver.find_element(By.XPATH, "//div[@class='pwd_error']").text
            # assert text == result
            assert text == result

