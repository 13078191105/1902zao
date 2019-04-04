from selenium import webdriver
from Common.Assert import Assertions
import time
import os
from Common.baseui import baseUI
from Common import baseui


class TestFirstUIDemo:

    def test_demo(self, driver):
        base = baseUI(driver)

        driver.get("http://192.168.60.132/login#/home")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        #         点击营销//span[text()='营销']

        base.click("点击营销", "//span[text()='营销']")
        # 点击优惠券列表//span[text()='优惠券列表']
        base.click("点击优惠券列表", "//span[text()='优惠券列表']")
        # 点击编辑
        base.click("点击编辑", "(//span[contains(text(),'编辑')])[1]")
        # 填写优惠券名称：//label[contains(text(),'优惠券名称：')]/following-sibling::div//input
        base.send_keys("填写优惠券名称", "//label[contains(text(),'优惠券名称：')]/following-sibling::div//input", "全场不通用")
        # 总发行量：//label[contains(text(),'总发行量：')]/following-sibling::div//input
        base.send_keys("填写总发行量", "//label[contains(text(),'总发行量：')]/following-sibling::div//input", "100")
        # 面额：//label[contains(text(),'面额：')]/following-sibling::div//input
        base.send_keys("填写面额", "//label[contains(text(),'面额：')]/following-sibling::div//input", "20")
        # 使用门槛：//label[contains(text(),'使用门槛：')]/following-sibling::div//input
        base.send_keys("填写使用门槛", "//label[contains(text(),'使用门槛：')]/following-sibling::div//input", "1000")
        # 点击提交//span[contains(text(),'提交')]
        base.click("点击提交", "//span[contains(text(),'提交')]")
        # 点击确定//span[contains(text(),'确定')]
        base.click("点击确定", "//span[contains(text(),'确定')]")
        # 断言
        # print(driver.page_source)
        xpath = driver.find_element_by_xpath("//div[@role='alert']/p")
        print(xpath)
        assertions = Assertions()
        # assertions.assert_in_text(driver.page_source, '修改成功')
        assertions.assert_in_text(xpath.text, '修改成功')



    def test_demo1(self,driver):
        base = baseUI(driver)

        driver.get("http://192.168.60.132/login#/home")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        #点击订单(//span[contains(text(),'订单')])[1]
        base.click("点击订单","//span[contains(text(),'订单')]")
        # 点击订单列表(//span[contains(text(),'订单列表')]
        base.click("点击订单列表", "//span[contains(text(),'订单列表')]")
        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击待发货//span[contains(text(),'待发货')]
        base.click("点击代发货", "//span[contains(text(),'待发货')]")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
        # 记录编号//tbody/tr[1]/td[2]/div
        num = base.get_text("第一条编号","//tbody/tr[1]/td[2]/div")
        # 记录订单编号
        order_num = base.get_text("点击第一条订单编号","//tbody/tr[1]/td[3]/div")
        # 点击第一条订单发货
        base.click("点击第一条订单发货","//tbody/tr[1]/td[10]/div/button[3]")
        # 选择物理公司//input[@readonly='readonly']
        base.click("选择物理公司", "//input[@readonly='readonly']")
        # 选择顺丰//span[contains(text(),'顺丰')]
        base.click("选择顺丰", "//span[contains(text(),'顺丰')]")
        # 输入订单编号
        base.send_keys("选择顺丰", "//*[@id='app']/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr/td[7]/div/div/input",'123456789')
        # 点击确定//span[contains(text(),'确定')]
        base.click("点击确定", "//span[contains(text(),'确定')]")
        # 点击确定(//span[contains(text(),'确定')])[2]
        base.click("点击确定", "(//span[contains(text(),'确定')])[2]")
        # 断言
        # print(driver.page_source)
        xpath = driver.find_element_by_xpath("//div[@role='alert']/p")
        # print(xpath.text)
        assertions = Assertions()
        assertions.assert_in_text(xpath.text,'发货成功!')







        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击已发货//span[text()='待发货']
        base.click("点击已发货", "//span[text()='已发货']")
        #输入订单编号//input[@placeholder='订单编号']
        base.send_keys("输入订单编号","//input[@placeholder='订单编号']",order_num)
        # 点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #定位到刚才发货的订单
        time.sleep(1)
        #通过xpath定位到一组元素，存到一个list中
        nums = driver.find_elements_by_xpath("(//tbody)[1]/tr/td[2]")
        #存放是否能找到编号 找到true  未找到 false
        b = False
        #遍历上边的list
        for n in nums:
            #n.text取出元素的可视文本
            print(n.text)
            #判断可视文本是否与发货订单的编号相同
            if n.text ==num:
                #如果相同，就讲true赋值给b
                b = True
        #断言，订单状态转换是否正确
        assert True == b
        time.sleep(3)



    def test_demo2(self,driver):
        base = baseUI(driver)
        # 打开网页
        driver.get("http://192.168.60.132/#/login")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录","//span[contains(text(),'登录')]")
        # 点击商品
        base.click("点击商品","(//span[contains(text(),'商品')])[1]")
        # 填写添加商品
        base.click("点击添加商品","(//span[contains(text(),'添加商品')])[1]")
        # 点击商品分类
        base.click("点击商品分类","(//label[contains(text(),'商品分类：')]/following-sibling::div//span)[4]")
        # 点击手机数码
        base.click("点击手机数码","//li[contains(text(),'手机数码')]")
        # 点击手机通讯
        base.click("点击手机通讯","//li[contains(text(),'手机通讯')]")
        # 输入商品名称
        base.send_keys("输入商品名称","//label[contains(text(), '商品名称：')]/following-sibling::div//input","三星")
        # 输入副标题
        base.send_keys("输入副标题","//label[contains(text(),'副标题：')]/following-sibling::div//input","XXX")
        # 点击商品品牌
        base.click("点击商品品牌","//label[contains(text(),'商品品牌：')]/following-sibling::div//input")
        # 点击三星
        base.click("点击三星","//span[contains(text(),'三星')]")
        # 商品介绍
        base.send_keys("填写商品介绍","//label[contains(text(),'商品介绍：')]/following-sibling::div//textarea","XXX")
        # 商品货号
        base.send_keys("填写商品货号","//label[contains(text(),'商品货号：')]/following-sibling::div//input","XXX")
        # 商品售价
        base.send_keys("填写商品售价","//label[contains(text(),'商品售价：')]/following-sibling::div//input","1000")
        # 市场价
        base.send_keys("填写市场价","//label[contains(text(),'市场价：')]/following-sibling::div//input","1001")
        # 商品库存
        base.send_keys("填写商品库存","//label[contains(text(),'商品库存：')]/following-sibling::div//input","11")
        # 计量单位
        base.send_keys("填写计量单位","//label[contains(text(),'计量单位：')]/following-sibling::div//input","个")
        # 商品重量
        base.send_keys("填写商品重量","//label[contains(text(),'商品重量：')]/following-sibling::div//input","8")
        # 排序
        base.send_keys("填写排序","//label[contains(text(),'排序')]/following-sibling::div//input","1")
        # 点击下一步
        base.click("点击下一步","//span[contains(text(),'下一步，填写商品促销')]")
        # 点击预告商品
        base.click("点击预告商品","//label[contains(text(),'预告商品：')]/following-sibling::div//span")
        # 点击商品上架
        base.click("点击商品上架","//label[contains(text(),'商品上架：')]/following-sibling::div//span")
        # 点击商品推荐
        base.click("点击商品推荐","(//label[contains(text(),'商品推荐：')]/following-sibling::div//span)[4]")
        # 点击服务保证
        base.click("点击服务保证","(//label[contains(text(),'服务保证：')]/following-sibling::div//span)[1]")
        # 点击特惠促销
        base.click("点击特惠促销","//span[contains(text(),'特惠促销')]")
        # 开始时间
        base.send_keys("填写开始时间","//div[contains(text(),'开始时间')]//following-sibling::div//input","2019-04-03 00:00:00")
        # 结束时间
        base.send_keys("填写结束时间","//div[contains(text(),'结束时间')]//following-sibling::div//input","2019-04-13 00:00:00")
        # 促销价格
        base.send_keys("填写促销价格","//div[contains(text(),'促销价格')]//following-sibling::div//input","998")
        # 下一步
        base.click("点击下一步","//span[contains(text(),'下一步，填写商品属性')]")
        # 属性类型(//label[contains(text(),'属性类型：')]/following-sibling::div//div)[1]
        base.click("点击属性类型","(//label[contains(text(),'属性类型：')]/following-sibling::div//div)[1]")
        # 点击手机数码//span[contains(text(),'手机数码')]
        base.click("手机数码-手机通讯","//span[contains(text(),'手机数码-手机通讯')]")
        # 添加商品规格(//div[contains(text(),'颜色：')]//following-sibling::div//input)[1]
        base.send_keys("添加商品规格","(//div[contains(text(),'颜色：')]//following-sibling::div//input)[1]","黑色")
        # 点击添加//span[contains(text(),'增加')]
        base.click("点击添加","//span[contains(text(),'增加')]")
        base.send_keys("添加商品规格", "(//div[contains(text(),'颜色：')]//following-sibling::div//input)[2]", "白色")
        base.click("点击添加", "//span[contains(text(),'增加')]")
        base.send_keys("添加商品规格", "(//div[contains(text(),'颜色：')]//following-sibling::div//input)[3]", "金色")
        base.click("点击添加", "//span[contains(text(),'增加')]")
        # 点击容量//div[contains(text(),'容量：')]//following-sibling::div//span
        base.click("点击容量","//div[contains(text(),'容量：')]//following-sibling::div//span")
        # 填写屏幕尺寸// div[contains(text(), '屏幕尺寸:')] // following - sibling::div // input
        base.send_keys("填写屏幕尺寸","//div[contains(text(),'屏幕尺寸:')]//following-sibling::div//input","8.8")
        # 点击网络
        base.click("点击网络","//div[contains(text(),'网络:')]//following-sibling::div//input")
        # 点击4G//span[(text()='4G')]
        base.click("点击4G","//span[(text()='4G')]")
        # 点击系统//div[contains(text(),'系统:')]//following-sibling::div//input
        base.click("点击系统","//div[contains(text(),'系统:')]//following-sibling::div//input")
        # 点击ios//span[(text()='IOS')]
        base.click("点击系统","//span[(text()='IOS')]")
        # 添加电池容量//div[contains(text(),'电池容量:')]//following-sibling::div//input
        base.send_keys("添加电池容量","//div[contains(text(),'电池容量:')]//following-sibling::div//input","10000")
        # 商品相册
        # 规格参数
        xpath = driver.find_element_by_xpath("(//iframe[contains(@id,'vue-tinymce')])[1]")
        driver.switch_to_frame(xpath)
        # 填写规格参数
        base.send_keys("填写规格参数", "//body[@id='tinymce']", "!!!!")
        driver.switch_to_default_content()
        base.click("点击下一步","//span[contains(text(),'下一步，选择商品关联')]")

        base.click("点击下一步","//span[contains(text(),'完成，提交商品')]")
        # 点击确定
        base.click("点击确定","//span[contains(text(),'取消')]")










