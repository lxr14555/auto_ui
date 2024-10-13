from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By

from po.base import Base
from po.event import Event


class TestLoginRegister:

    @pytest.mark.parametrize(("username", "password", "result"), [
        ("test123", "test123", "欢迎您：test123 | 退出"),
        ("test12", "test12", "用户名错误"),
        ("test123", "test12", "密码错误")
    ], ids=(
            "test_shopping_mall_01",
            "test_shopping_mall_02",
            "test_shopping_mall_03"
    ))
    @allure.feature('登录注册')
    @allure.story('登录')
    def test_shopping_mall(self, username, password, result, open_homepage):
        driver = open_homepage
        Event().event_login(driver, username, password)
        if '欢迎您' in result:
            text = driver.get_text((By.XPATH, "//div[@class='login_btn fl']"))
            driver.sel_click((By.XPATH, "//a[contains(text(),'退出')]"))
            assert text == result
        elif '用户名错误' in result:
            text = driver.get_text((By.XPATH, "//div[@class='user_error']"))
            assert text != result
        elif '密码错误' in result:
            text = driver.get_text((By.XPATH, "//div[@class='pwd_error']"))
            assert text == result
        sleep(1)
