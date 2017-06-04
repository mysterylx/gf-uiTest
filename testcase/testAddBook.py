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

    '''添加前检查是否存在id=1000的对象，若存在先删除'''
    def beginAdd(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        bookTable = driver.find_element_by_xpath(elementLocation.TABLE_BOOKLIST)
        try:
            bookTable.find_element_by_xpath(elementLocation.BOOK_1000)
            book = bookTable.find_element_by_xpath(elementLocation.BOOK_1000)
            book.click()
            time.sleep(2)
            delButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKDEL)
            delButton.click()
            time.sleep(2)
            message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
            isDeleted = message.find_element_by_xpath(elementLocation.BUTTON_YES)
            isDeleted.click()
            time.sleep(2)
            driver.find_element_by_xpath(elementLocation.BUTTON_OK).click()
        except Exception, e:
            pass

    '''添加id=1000的book，预期添加成功'''
    def testAddBook(self):
        self.beginAdd()
        driver = self.driver
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        addButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKADD)
        addButton.click()
        time.sleep(2)

        bookInfo = driver.find_element_by_xpath(elementLocation.DIV_BOOKADD_INFO);
        bookId = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKID)
        bookName = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKNAME)
        bookAuthor = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKAUTHOR)
        bookYear = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKYEAR)
        bookdesc = bookInfo.find_element_by_xpath(elementLocation.INPUT_DESC)

        bookId.send_keys("1000")
        bookName.send_keys("test")
        bookAuthor.send_keys("test")
        bookYear.send_keys("2017")
        bookdesc.send_keys("test")

        submit = driver.find_element_by_xpath(elementLocation.BUTTON_SUBMIT)
        submit.click()
        time.sleep(2)

        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        messageValue = message.find_element_by_xpath(elementLocation.DIV_MESSAGE_VALUE)
        assert messageValue.text == u'添加书籍成功'
        driver.find_element_by_xpath(elementLocation.BUTTON_OK).click()

    '''添加id已经存在的book，预期添加失败'''
    def testAddSameBook(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        addButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKADD)
        addButton.click()
        time.sleep(2)

        bookInfo = driver.find_element_by_xpath(elementLocation.DIV_BOOKADD_INFO);
        bookId = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKID)
        bookName = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKNAME)
        bookAuthor = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKAUTHOR)
        bookYear = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKYEAR)
        bookdesc = bookInfo.find_element_by_xpath(elementLocation.INPUT_DESC)

        bookId.send_keys("1000")
        bookName.send_keys("test")
        bookAuthor.send_keys("test")
        bookYear.send_keys("2017")
        bookdesc.send_keys("test")

        submit = driver.find_element_by_xpath(elementLocation.BUTTON_SUBMIT)
        submit.click()
        time.sleep(2)

        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        messageValue = message.find_element_by_xpath(elementLocation.DIV_MESSAGE_VALUE)
        assert messageValue.text == u'errorNo:1,errorInfo:该id已存在。'

    def tearDown(self):
        self.driver.close()