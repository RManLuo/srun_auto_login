#!/usr/bin/python3
# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019/9/16 21:45
# @Author   : Raymond Luo
# @File     : auto_login.py
# @User     : luoli
# @Software: PyCharm
# Reference:**********************************************
import os
import config
import time
import logging
import platform
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutoLogin(object):
    def __init__(self, username, password, wifi):
        '''
        构建登录信息
        :param username: 用户名
        :param password: 密码
        :param wifi: wifi模式
        '''
        self.username = username
        self.password = password
        self.wifi = wifi
        self.login_gateway = "http://10.0.10.66/srun_portal_pc.php" if wifi == "utsz" else "http://10.248.98.2/srun_portal_pc?ac_id=1&theme=basic2"  # 设置网关

        if config.log:  # 记录log
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(level=logging.INFO)
            handler = logging.FileHandler(os.path.join(config.log_path, "log.txt"))
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            if config.debug:  # debug 在控制台输出
                console = logging.StreamHandler()
                console.setLevel(logging.INFO)
                self.logger.addHandler(console)

        if wifi == 'hitsz':  # 设置Chrome
            self.chrome_options = Options()
            self.chrome_options.add_argument('--headless')
            self.chrome_options.add_argument('--disable-gpu')
            operating_system = platform.platform()
            # 根据操作系统获取driver version 77
            if 'Windows' in operating_system:
                self.path = 'webdriver/chromedriver_win32.exe'
            elif 'Mac' in operating_system:
                self.path = 'webdriver/chromedriver_mac64'
            elif 'Linux' in operating_system:
                self.path = 'webdriver/chromedriver_linux64'
            else:
                self.logger.warning("Not support this system :{}".format(operating_system))
                raise Exception("Not support this system :{}".format(operating_system))

    def _check_network(self):
        '''
        检查网络是否畅通
        :return: Ture为畅通，False为不畅通。
        '''
        try:
            req = requests.get('http://www.baidu.com', timeout=5)
            if 'baidu' in req.text:
                return True
            else:
                return False
        except:
            return False

    def _login_utsz(self):
        '''
        登录utsz
        :return:
        '''
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        }
        data = {'action': 'login', 'username': self.username, 'password': self.password, "ac_id": 1}
        req = requests.post(self.login_gateway, headers=header, data=data)
        return

    def _login_hitsz(self):
        '''
        登录hitsz
        :return:
        '''
        driver = webdriver.Chrome(executable_path=self.path, chrome_options=self.chrome_options)
        driver.set_page_load_timeout(10)
        driver.set_script_timeout(10)  # 超时
        try:
            driver.get(self.login_gateway)
        except:
            self.logger.warning("Get gatway out of time....try again soon")
            return
        time.sleep(2)
        username_box = driver.find_element_by_xpath('//*[@id="username"]')
        password_box = driver.find_element_by_xpath('//*[@id="password"]')
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        driver.find_element_by_xpath('//*[@id="login"]').click()  # 登录
        time.sleep(3)  # 等那个sb回调json
        driver.quit()
        return

    def _login(self):
        '''
        登录网络
        :return: 成功返回True 失败返回 False
        '''
        i = 1
        while i <= config.retry:
            self.logger.info("Start trying times: {}".format(i))
            if self.wifi == "utsz":
                self._login_utsz()
            else:
                self._login_hitsz()
            time.sleep(5)
            status = self._check_network()
            if status:
                self.logger.info("Loging success")
                return True
            else:
                i += 1
                time.sleep(10)  # 等10秒再尝试
        if i > config.retry:
            self.logger.warning("Out of trying times")
            raise Exception("Out of trying times")

    def start(self):
        self.logger.info("Start watching network status")
        while True:
            # check是否掉线
            self.logger.info("Checking network")
            if self._check_network():
                self.logger.info("Network is good")
            else:
                self.logger.info("Network is disconnected. Try login now.")
                self._login()  # 重新登录
            time.sleep(config.check_time)


if __name__ == "__main__":
    login = AutoLogin(config.username, config.passowrd, config.wifi)
    login.start()
