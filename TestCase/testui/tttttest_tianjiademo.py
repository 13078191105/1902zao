from selenium import webdriver
import time
import os
from Common.Assert import Assertions
from Common.baseui import *
from Common.baseui import baseUI

#打开浏览器
#确定chromedriver.exe的位置
class TestFirstUIDemo:
    def test_demo(self,driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # time.sleep(1)
        # 输入用户名
        base.send_keys("输入用户名","//input [@name='username']","admin")
        # 输入密码
        base.send_keys("输入密码","//input [@name='password']","123456")

        # 点击登录
        base.click("点击登录","//span[contains(text(),'登录')]")

        # 点击商品
        base.click("点击商品","(//span[contains(text(),'商品')])[1]")

        # 点击添加商品
        base.click("点击添加商品","(//span[contains(text(),'添加商品')])[1]")

        # 点击商品分类
        base.click("点击商品分类","//span[@class='el-cascader__label']")

        # 点击商品分类
        base.click("点击商品分类","//li[contains(text(),'服装')]")

        # 点击外套
        base.click("点击外套","//li[contains(text(),'外套')]")

        # 商品名称
        base.send_keys("输入商品名称","//label[contains(text(),'商品名称：')]/following-sibling::div//input","衣服")

        #添加副标题
        base.send_keys("添加副标题","//label[contains(text(),'副标题：')]/following-sibling::div//input","衣服")

        #        添加商品品牌
        base.click("添加商品品牌","//label[contains(text(),'商品品牌：')]/following-sibling::div//div")

        # 选择海澜之家
        base.click("点击海澜之家","//span[text()='小米']")

        #下一步
        base.click("点击下一步,填写商品促销","//span[text()='下一步，填写商品促销']")


        # 赠送积分//label[contains(text(),'赠送积分：')]/following-sibling::div//input
        base.send_keys("输入赠送积分","//label[contains(text(),'赠送积分：')]/following-sibling::div//input","200")

        # 赠送成长值//label[contains(text(),'赠送成长值：')]/following-sibling::div//input
        base.send_keys("输入赠送成长值","//label[contains(text(),'赠送成长值：')]/following-sibling::div//input","100")

        # 积分购买限制//label[contains(text(),'积分购买限制：')]/following-sibling::div//input
        base.send_keys("输入积分购买限制","//label[contains(text(),'积分购买限制：')]/following-sibling::div//input","50")

        # 预告商品//label[contains(text(),'预告商品：')]/following-sibling::div//span
        base.click("预告商品","//label[contains(text(),'预告商品：')]/following-sibling::div//span")

        # 点击商品上架
        base.click("点击商品上架","//label[contains(text(),'商品上架：')]/following-sibling::div//span")

        # 点击商品推荐
        base.click("点击商品推荐","(//label[contains(text(),'商品推荐：')]/following-sibling::div//span)[4]")

        # 点击服务保证
        base.click("点击服务保证","(//label[contains(text(),'服务保证：')]/following-sibling::div//span)[1]")

        # 详细页标题//label[contains(text(),'详细页标题：')]/following-sibling::div//input
        base.send_keys("输入详细页标题","//label[contains(text(),'详细页标题：')]/following-sibling::div//input","好吃")


        # 详细页描述//label[contains(text(),'详细页描述：')]/following-sibling::div//input
        base.send_keys("输入详细页描述","//label[contains(text(),'详细页描述：')]/following-sibling::div//input","超好吃")

        # 商品关键字//label[contains(text(),'商品关键字：')]/following-sibling::div//input
        base.send_keys("//label[contains(text(),'商品关键字：')]/following-sibling::div//input","超级好吃")

        time.sleep(1)
        # 下一步，填写商品属性
        xiayibu = driver.find_element_by_xpath("//span[contains(text(),'下一步，填写商品属性')]")
        xiayibu.click()
        time.sleep(1)
        # 下一步，选择商品关联
        xiayibu = driver.find_element_by_xpath("//span[contains(text(),'下一步，选择商品关联')]")
        xiayibu.click()
        time.sleep(1)
        # 完成，提交商品
        xiayibu = driver.find_element_by_xpath("//span[contains(text(),'完成，提交商品')]")
        xiayibu.click()
        time.sleep(1)























