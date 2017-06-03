# -*- coding: UTF-8 -*-
from selenium import webdriver

import config


class Driver():
    def __init__(self):
        self.driver = None


class FireFoxWebDriver(Driver):
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=config.GECKODRIVER)

    def getDriver(self):
        return self.driver


class DriverFactory():
    def creater(self,type):
        if type == 'FireFox':
            driver = FireFoxWebDriver()
        else:
            driver = None
        return driver