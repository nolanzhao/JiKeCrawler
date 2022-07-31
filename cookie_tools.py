import os
import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import BASE_URL, LOGIN_URL, BASE_DIR, CHROMEDRIVER_PATH


def get_driver():
    try:
        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9222"
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(60)
        time.sleep(1)
        return driver
    except:
        raise Exception("启动Chrome失败!")


def retrive_cookie(cookies):
    d = {}
    for c in cookies:
        d[c['name']] = c['value']
    res = f"_ga={d['_ga']}; _gid={d['_gid']}; fetchRankedUpdate={d['fetchRankedUpdate']}; x-jike-access-token={d['x-jike-access-token']}; x-jike-refresh-token={d['x-jike-refresh-token']}"
    return res


def save_cookie(cookie):
    filePath = os.path.join(BASE_DIR, 'COOKIE')
    with open(filePath, "w") as f:
        f.write(cookie)


def login(driver):
    driver.get(LOGIN_URL)
    mobile = input(">> mobile:")
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys(
        mobile)  # 输入手机号
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]").click()  # 发送验证码
    verify_code = input(">> verify_code:")
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/input[1]").send_keys(
        verify_code)  # 填写验证码
    driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/label[1]/div[1]/*[name()='svg'][2]"
    ).click()  # 勾选同意《用户协议》
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()  # 点击登录
    time.sleep(2)


def init_cookie():
    driver = get_driver()
    do_login = input(">> 是否重新登录? (y / N)\n")
    if do_login == 'Y' or do_login == 'y':
        login(driver)
    driver.get(BASE_URL)
    time.sleep(2)
    cookie = retrive_cookie(driver.get_cookies())
    if cookie is None:
        print("No cookie found.")
        return
    print(cookie)
    save_cookie(cookie)


if __name__ == "__main__":
    init_cookie()