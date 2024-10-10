from selenium import webdriver


def login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()