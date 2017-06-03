# -*- coding: UTF-8 -*-
import time
import unittest

import config
from conf import elementLocation
from lib import webDriver


class Test(unittest.TestCase):

    def setUp(self):

        self.driver = webDriver.DriverFactory().creater('FireFox').getDriver()
        self.driver.implicitly_wait(30)
        self.driver.get(config.URL)
        time.sleep(2)

    def testDeleteBook(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        bookTable = driver.find_element_by_xpath(elementLocation.TABLE_BOOKLIST)
        book = bookTable.find_element_by_xpath(elementLocation.TABLE_FIRSTBOOK) # 获取列表里面第一本书
        book.click()
        time.sleep(2)
        delButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKDEL)
        delButton.click()
        time.sleep(2)
        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        isdeleted  = message.find_element_by_xpath(elementLocation.BUTTON_YES)
        isdeleted.click()
        time.sleep(2)
        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        messageValue = message.find_element_by_xpath(elementLocation.DIV_MESSAGE_VALUE)
        assert messageValue.text == u'删除书籍成功！'
        driver.find_element_by_xpath(elementLocation.BUTTON_OK).click()

    def tearDown(self):
        self.driver.close()
