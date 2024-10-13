class ENV:
    url = 'http://127.0.0.1:8000/'
    user_name = 'test123'
    pass_word = 'test123'

class DBSql:
    """
    初始化时清除数据sql语句
    清空：用户、购物车、订单信息
    并插入：测试用户 test123456
    """
    # sql_file = rf'\\{ENV.host_ip}\daily_fresh_demo-master\db.sqlite3'  # 另一台电脑
    sql_file = rf'D:\Dev\pythonProject\ShoppingMall\daily_fresh_demo-master\db.sqlite3'  # 本地
    # D:\电子商城系统\daily_fresh_demo-master\db.sqlite3
    sql_list = [
        'DELETE FROM df_order_orderdetailinfo',
        'DELETE FROM df_order_orderinfo',
        'DELETE FROM df_user_userinfo',
        'DELETE FROM df_cart_cartinfo',
        "INSERT INTO 'df_user_userinfo' VALUES ('46', 'test123456', 'fb15a1bc444e13e2c58a0a502c74a54106b5a0dc', 'sadfasdfasd@qq.com', '', '', '', '');",
        "INSERT INTO 'df_user_userinfo' VALUES ('41', 'test123', '7288edd0fc3ffcbe93a0cf06e3568e28521687bc', 'sad333fasd@qq.com', '', '', '', '');"
    ]