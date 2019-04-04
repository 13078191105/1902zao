# 如何使用pytest 做测试
# 1 设置pycharm
# 2 新建模块：以test_开头
# 3 新建类 以Test 开头
# 4 在类中新建方法 以 test_开头
# @ 开头的

import allure

@allure.feature("类上装饰器")
class Testlz:
    @allure.story("max方法上的")
    def test_Max_(self):
        assert 1<2

    @allure.story("max1方法上的")
    def test_Max1(self):
        assert 3>2

    @allure.story("max2方法上的")
    def test_Max2(self):
        assert 5>2
