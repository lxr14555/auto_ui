from time import sleep

import allure
from selenium.webdriver.common.by import By

from common.log import log
from settings import ENV


class Event:
    @staticmethod
    @allure.step('登录')
    def event_login(driver, username, password):
        try:
            driver.get(ENV.url)
            driver.sel_click((By.XPATH, "//a[contains(text(),'登录')]"))
            # sleep(1)
            # driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名']").send_keys(username)
            driver.sel_send_keys((By.XPATH, "//input[@placeholder='请输入用户名']"), username)
            # sleep(1)
            # driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']").send_keys(password)
            driver.sel_send_keys((By.XPATH, "//input[@placeholder='请输入密码']"), password)
            sleep(1)
            # driver.find_element(By.XPATH, "//input[@value='登录']").click()
            driver.sel_click((By.XPATH, "//input[@value='登录']"))
        except Exception as e:
            log.error(f'登录异常，为：{e}')
            raise e

    @staticmethod
    @allure.step('新增收货地址')
    def add_address(driver, ushou='张三', uphone='18827373333', uyoubian='998889', uaddress='人民路10号'):
        driver.get(ENV.url)
        driver.sel_click((By.XPATH, "//a[contains(text(),'用户中心')]"))  # 点击用户中心
        driver.sel_click((By.XPATH, "//a[contains(text(),'收货地址')]"))
        driver.sel_send_keys((By.XPATH, "//input[@name='ushou']"), ushou)
        driver.sel_send_keys((By.XPATH, "//input[@name='uphone']"), uphone)
        driver.sel_send_keys((By.XPATH, "//input[@name='uyoubian']"), uyoubian)
        driver.sel_send_keys((By.XPATH, "//textarea[@name='uaddress']"), uaddress)
        driver.sel_click((By.XPATH, "//input[@value='修改地址']"))

    @staticmethod
    @allure.step('点击立即购买并提交订单')
    def event_submit_order(driver):
        try:
            driver.get(ENV.url + '18/')
            driver.sel_click((By.XPATH, "//a[@id='buy_now']"))
            sleep(1)
            driver.sel_click((By.XPATH, "//a[contains(text(),'去结算')]"))
            sleep(1)
            driver.sel_click((By.XPATH, "//a[@id='order_btn']"))
            sleep(1)
        except Exception as e:
            log.error(f'立即购买并点击提交订单事件异常，为：{e}')
            raise e

