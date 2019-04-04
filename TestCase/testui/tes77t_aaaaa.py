from selenium import webdriver
from Common.Assert import Assertions
import time
import os
from Common.baseui import baseUI
from Common import baseui
# from Common.baseuii import *

class TestFirstUIDemo:
    def test_demo(self,driver):
        base = baseUI(driver)

        driver.get("http://192.168.60.132/login#/home")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
#         点击营销//span[text()='营销']

        base.click("点击营销","//span[text()='营销']")
        # 点击优惠券列表//span[text()='优惠券列表']
        base.click("点击优惠券列表","//span[text()='优惠券列表']")
        # 点击编辑
        base.click("点击编辑","(//span[contains(text(),'编辑')])[1]")
        #填写优惠券名称：//label[contains(text(),'优惠券名称：')]/following-sibling::div//input
        base.send_keys("填写优惠券名称","//label[contains(text(),'优惠券名称：')]/following-sibling::div//input","全场不通用")
        # 总发行量：//label[contains(text(),'总发行量：')]/following-sibling::div//input
        base.send_keys("填写总发行量","//label[contains(text(),'总发行量：')]/following-sibling::div//input","100")
        # 面额：//label[contains(text(),'面额：')]/following-sibling::div//input
        base.send_keys("填写面额","//label[contains(text(),'面额：')]/following-sibling::div//input","20")
        # 使用门槛：//label[contains(text(),'使用门槛：')]/following-sibling::div//input
        base.send_keys("填写使用门槛","//label[contains(text(),'使用门槛：')]/following-sibling::div//input","1000")
        # 点击提交//span[contains(text(),'提交')]
        base.click("点击提交","//span[contains(text(),'提交')]")
        # 点击确定//span[contains(text(),'确定')]
        base.click("点击确定","//span[contains(text(),'确定')]")
        # 断言
        # print(driver.page_source)
        xpath = driver.find_element_by_xpath("//div[@role='alert']/p")
        print(xpath)
        assertions = Assertions()
        # assertions.assert_in_text(driver.page_source, '修改成功')
        assertions.assert_in_text(xpath.text,'修改成功')