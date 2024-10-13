import os
import time

from selenium import webdriver
import re
from time import sleep
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import log
from common.sql import MysqlAuto
from config.conf import ALLURE_IMG_DIR
from settings import DBSql


class Base:
    """初始化driver、清除数据、封装selenium操作（第3层）"""

    def __init__(self, driver=None):
        if driver:
            # 后续复用即可
            self.driver = driver
        else:
            # 首次为none，打开一个页面
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

            # 初始化数据（删掉所有用户和订单信息，并创建全新的测试账号【test123456】
            MysqlAuto().execute(DBSql.sql_list)

    def get(self, url):
        """
        重写方法，使其支持额外的功能
        """
        try:
            self.driver.get(url)
            return self.driver
        except Exception as e:
            raise e

    def quit(self):
        """
        重写方法，使其支持额外的功能
        """
        try:
            self.driver.quit()
        except Exception as e:
            raise e

    def alert_text(self):
        """
        重写switch_to方法，使其支持额外的功能
        """
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            log.info(text)
            alert.accept()
            return text
        except Exception as e:
            raise e

    def click_alert(self):
        """点击alert确定"""
        try:
            # 切换到alert
            alert = self.driver.switch_to.alert
            # 点击 Alert 上的按钮
            alert.accept()  # 点击确认按钮
        except Exception as e:
            raise e

    @allure.step('鼠标左键单击')
    def sel_click(self, sel, timeout=20):
        """
        鼠标左键单击（元素中是否可见并且是enable的，代表可点击）
        https://www.cnblogs.com/an5456/p/11279879.html  这篇内容写的较详细
        """
        try:
            # WebDriverWait(drive, timeout).until(expected_conditions.element_to_be_clickable((by, sel))).click()
            WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((sel))).click()
            sleep(0.2)
            selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
            if len(selen) > 0:
                log.info(f"点击：{selen}")
            return True
        except Exception as e:
            log.error(f"无法定位到该元素：{sel}，异常为：\n{e}")
            raise e

    @allure.step('元素可点击')
    def elements_clickable(self, by, sel, timeout=30):
        try:
            # https://www.cnblogs.com/an5456/p/11279879.html 参考这篇文章
            WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((by, sel)))
            return True
        except Exception as e:
            log.error(f"已达到超时时间元素【{sel}】仍未加载出，不可点击，异常为：{e}")
            raise e

    @allure.step('元素可见')
    def elements_visibility(self, drive, by, sel, timeout=30):
        try:
            # https://www.cnblogs.com/an5456/p/11279879.html 参考这篇文章
            WebDriverWait(drive, timeout).until(expected_conditions.visibility_of_element_located((by, sel)))
            return True
        except Exception as e:
            log.error(f"已达到超时时间元素仍然不可见，异常为：{e}")
            raise e

    @allure.step('输入内容')
    def sel_send_keys(self, sel, value, timeout=10):
        """
        输入内容
        """
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((sel))).clear()
            sleep(0.2)
            WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((sel))).send_keys(
                value)
            sleep(0.2)
            selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
            if len(selen) > 0:
                log.info(f"点击：{selen}输入：{value}")
            return True
        except Exception as e:
            log.error(f"无法定位到该元素：{sel}，异常为：\n{e}")
            raise e

    @allure.step('获取指定元素的text值')
    def get_text(self, els, timeout=10, mode=0):
        """获取指定元素的text值"""
        try:
            # 等待元素在页面上出现
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((els))
            )
            if mode == 0:
                log.info(element.text)
                return element.text
            elif mode == 1:
                log.info(element.get_attribute('textContent'))
                return element.get_attribute('textContent')
        except Exception as e:
            print(f"错误：{e}")
            return None

    def allure_save_screenshot(self, name):
        """
        allure添加截图附件（使用Chrome自带截图）
        :return:
        """
        with open(self.chrom_save_screenshot(), "rb") as f:
            log.info('网页截图')
            allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.JPG)

    @allure.step('chrom自带截图')
    def chrom_save_screenshot(self):
        print('==========================')
        """
        chrom自带截图
        """
        try:
            img_dir = ALLURE_IMG_DIR
            str_time = str(time.time())[:10]
            img_file = ALLURE_IMG_DIR + f'\\tmp_chrom_save_screenshot{str_time}.jpg'
            if not os.path.isdir(img_dir):
                os.makedirs(img_dir)
                log.info(f'创建目录：{img_dir}')
            sleep(1)
            self.driver.save_screenshot(img_file)
            return img_file
        except Exception as e:
            log.error(f'截图发生异常：{e}')
            raise