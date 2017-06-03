# -*- coding: UTF-8 -*-

# 左侧图书管理的xpath
BOOKMANAGER='//*[@id="treeview-1015-record-book_manage"]'

# 增删改 按钮的xpath
BUTTON_BOOKADD = '//*[text()="添加"]'
BUTTON_BOOKDEL = '//*[text()="删除"]'
BUTTON_BOOKUPDATE = '//*[text()="修改"]'
BUTTON_YES = '//*[text()="Yes"]'
BUTTON_OK = '//*[text()="OK"]'

# 增加，修改 弹层的xpath
DIV_BOOKADD_INFO = '//*[text()="添加book"]'

DIV_BOOKUPDATE_INFO = '//*[text()="编辑book"]'

# 图书列表的xpath
TABLE_BOOKLIST = '//*[@id="gridview-1043-table"]'
TABLE_FIRSTBOOK = '//*[@id="gridview-1043-body"]/child::tr'

# 增加，修改 弹层内图书信息输入框的xpath
INPUT_BOOKID='//*[@id="numberfield-1053-inputEl"]'
INPUT_BOOKNAME='//*[@id="textfield-1054-inputEl"]'
INPUT_BOOKAUTHOR='//*[@id="textfield-1055-inputEl"]'
INPUT_BOOKYEAR='//*[@id="numberfield-1056-inputEl"]'
INPUT_DESC='//*[@id="textarea-1057-inputEl"]'

# 增加，修改 弹层内提交按钮
BUTTON_SUBMIT= '//*[text()="提交"]'

# 信息框
DIV_MESSAGE = '//*[@id="messagebox-1001"]'
DIV_MESSAGE_VALUE = '//*[@id="messagebox-1001-displayfield-inputEl"]'


#
BOOK_1000 = '//*[@id="gridview-1043-record-1000"]'