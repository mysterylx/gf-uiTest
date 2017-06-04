# -*- coding: UTF-8 -*-
import time
import unittest

import config
from conf import elementLocation
from lib import webDriver


class Test(unittest.TestCase):

    def setUp(self):
        self.driverFactory = webDriver.DriverFactory()
        self.driver = self.driverFactory.creater('FireFox').getDriver()
        self.driver.implicitly_wait(30)
        self.driver.get(config.URL)
        time.sleep(2)

    '''修改列表中第一本book的bookName，为保障列表存在book，此case在addbook后执行'''
    def testUpdateBook(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        bookList = driver.find_element_by_xpath(elementLocation.TABLE_BOOKLIST)
        book = bookList.find_element_by_xpath(elementLocation.TABLE_FIRSTBOOK)  # 获取列表里面第一本书
        book.click()
        time.sleep(2)

        updateButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKUPDATE)
        updateButton.click()
        time.sleep(2)

        bookInfo = driver.find_element_by_xpath(elementLocation.DIV_BOOKUPDATE_INFO);
        bookName = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKNAME)
        bookName.clear()
        bookName.send_keys("lixiantest")
        submit = driver.find_element_by_xpath(elementLocation.BUTTON_SUBMIT)
        submit.click()

        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        messageValue = message.find_element_by_xpath(elementLocation.DIV_MESSAGE_VALUE)
        assert messageValue.text == u'更新成功'
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
