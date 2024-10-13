from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.sql import MysqlAuto
from po.event import Event
from settings import DBSql


class TestShoppingMall:
    def test_shopping_mall_013(self, login):
        # 初始化driver实例
        driver = login
        # 初始化数据，确保无地址，无订单
        MysqlAuto().execute(DBSql.sql_list)
        # 新增收货地址
        Event.add_address(driver)
        # 点击立即购买并提交订单
        Event.event_submit_order(driver)
        # 查询数据库订单
        sql = ['select * from df_order_orderinfo']
        order_list = MysqlAuto().execute(sql)
        assert len(order_list) == 1
        # 查询页面订单信息
        order_id = order_list[0][0]
        text = driver.get_text((By.XPATH, "/html/body/div[3]/div[2]/ul/li[2]"))
        text = driver.get_text((By.CSS_SELECTOR, "body > div.main_con.clearfix > div.right_content.clearfix > ul > "
                                                 "li:nth-child(2)"))
        # text = driver.get_text((By.XPATH, "//ul[@class='order_list_th w987 clearfix']"))
        print(order_id, '_____', text)
        assert order_id in text

        sleep(3)








