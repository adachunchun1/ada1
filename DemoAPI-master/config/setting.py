#! /usr/bin/python3
# _*_ coding:utf-8 _*_
__author__ = 'qichunchun'

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG =  os.path.join(BASE_DIR,"database","config.ini")
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR,"database","DemoAPITestCase_bak.xlsx")
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","DemoAPITestCase_bak.xlsx")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"testcase")
