# -*- coding: utf-8 -*-
# @project: daily_fresh_demo-master
# @file： sql_tmp.py
# @微信：super_lizxx
# @Author：测试小志
import sqlite3

from common.log import log
from settings import ENV, DBSql


class MysqlAuto(object):
    def __init__(self):
        """连接到SQLite数据库"""
        self.conn = sqlite3.connect(DBSql.sql_file)
        # 创建一个Cursor对象并作为属性，用于执行SQL命令
        self.cursor = self.conn.cursor()
        log.info(f"Connected to database: {DBSql.sql_file}")

    def __del__(self):
        """对象资源被释放时触发，在对象即将被删除时的最后操作"""
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
        log.info('Database connection closed.')

    def execute(self, sql_list):
        """执行SQL语句"""
        try:
            for i in sql_list:  # 语句列表
                log.info(f'sql：{i}')
                self.cursor.execute(i)
            result = self.cursor.fetchall()

            # 提交事务：
            self.conn.commit()
            return result
        except Exception as e:
            log.error(f'执行sql出现错误，异常为{e}')
            raise e


if __name__ == '__main__':
    """
    df_cart_cartinfo
    df_goods_goodsinfo
    df_goods_typeinfo
    df_order_orderdetailinfo        #清空
    df_order_orderinfo          #清空
    df_user_goodsbrowser
    df_user_userinfo        #清空
    """
    sql = ['select * from df_cart_cartinfo']
    # # del_sql = 'DELETE FROM df_order_orderinfo;'
    # # MysqlAuto().execute(DBSql.sql_list)
    # # sql = ['select * from df_cart_cartinfo']
    # # order_id = MysqlAuto().execute(sql)
    # # log.info(order_id)
    # # log.info(len(order_id))
    #
    res = MysqlAuto().execute(sql)
    print('__________________', res)
    # MysqlAuto().execute(DBSql.sql_list)
