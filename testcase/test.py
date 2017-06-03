# -*- coding: UTF-8 -*-
import time
import unittest

import config
from conf import elementLocation
from lib import webDriver


class Test(unittest.TestCase):

    def setUp(self):

        self.driver = webDriver.DriverFactory().creater('FireFox').getDriver()
        self.driver.get(config.URL)
        time.sleep(2)

    def testShowBooks(self):
        driver = self.driver
        driver.find_element_by_id("treeview-1015-record-book_manage").click()
        bookManageTab1 = driver.find_element_by_id("tab-1051")

    def testAddBook(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        addButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKADD)
        addButton.click()
        time.sleep(2)

        bookInfo = driver.find_element_by_xpath(elementLocation.DIV_BOOKADD_INFO);
        bookid = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKID)
        bookName = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKNAME)
        bookAuthor = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKAUTHOR)
        bookYear = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKYEAR)
        bookdesc = bookInfo.find_element_by_xpath(elementLocation.INPUT_DESC)

        bookid.send_keys("1000000")
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

    def testAddSameBook(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        addButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKADD)
        addButton.click()
        time.sleep(2)

        bookInfo = driver.find_element_by_xpath(elementLocation.DIV_BOOKADD_INFO);
        bookid = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKID)
        bookName = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKNAME)
        bookAuthor = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKAUTHOR)
        bookYear = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKYEAR)
        bookdesc = bookInfo.find_element_by_xpath(elementLocation.INPUT_DESC)

        bookid.send_keys("1000000")
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
        message = driver.find_element_by_id(elementLocation.DIV_MESSAGE)
        isdeleted  = message.find_element_by_xpath('//*[@id="button-1006-btnIconEl"]')
        isdeleted.click()
        time.sleep(2)
        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        messageValue = message.find_element_by_xpath(elementLocation.DIV_MESSAGE_VALUE)
        assert messageValue.text == u'删除书籍成功！'

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
        pass
        # self.driver.close()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test('testAddBook'))
    runner = unittest.TextTestRunner()
    runner.run(testunit)

    # fp = open('./result.html', 'wb')
    #
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test_report', description='test_desc')
    # runner.run(testunit)
    # fp.close()