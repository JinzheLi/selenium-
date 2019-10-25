#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 14:31
# @Author  : Aries
# @Site    : 
# @File    : 自动登录.py
# @Software: PyCharm
import requests
from selenium import webdriver
from requests.exceptions import RequestException


class LogOn:
    def __init__(self):
        self._username = None
        self._password = None
        self.url = None

    def getPage(self):
        """爬取页面信息"""
        assert self.url is not None, '请先调用fit函数'

        try:
            res = requests.get(self.url)
            if res.status_code == 200:
                return res.text
            else:
                return None
        except RequestException:
            return None

    def fit(self, url):
        self.url = url
        _data = []

        # 后期可以改成从数据库中读取上网用户的账号和密码，可以使用md5加密信息
        try:
            file_path = './info/user.txt'
            for line in open(file_path):
                _data.append(line)
        except Exception:
            print('缺少数据文件')

        try:
            self._username = _data[0]
            self._password = _data[1]
        except Exception:
            print('缺少用户名或密码')

    def log(self):
        if self.getPage() is None:
            print('请检查网络连接')
            return

        return self.operation()

    def operation(self):
        """登录操作函数"""
        # 无弹窗
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.add_argument('--headless')
        driver = webdriver.Firefox(options=firefoxOptions)

        '''
        # 创建浏览器对象
        driver = webdriver.Firefox()
        '''

        driver.get(self.url)

        input = driver.find_element_by_id('username')
        input.send_keys(self._username)

        input = driver.find_element_by_id('password')
        input.send_keys(self._password)

        botton = driver.find_element_by_class_name('btn_class')
        botton.click()

        try:
            if driver.find_element_by_class_name('a_demo_one'):
                return 'success'

        except Exception:
            return 'Fail Password or Username'


if __name__ == '__main__':
    url = 'http://10.1.1.131:902/srun_portal_pc.php?ac_id=1&'
    logon = LogOn()
    logon.fit(url)
    print(logon.log())
