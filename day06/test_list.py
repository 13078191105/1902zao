import allure
import pytest
from Common import Assert
from Common import Request
from Common import read_excel

assertions = Assert.Assertions()
request = Request.Request()
read_excel.read_excel_list('./')
@allure.feature("演示模块")
class Testdemo(object):

    @allure.story("演示功能")
    @pytest.mark.parametrize("pwd,name,msg",
                             [('123456','admin','成功'),('1234561','admin','错误'),('123456','admin1','错误')],
                             ids=['登录成功','密码错误','用户名错误'])
    def test_case_demo(self,pwd,name,msg):
        login_data = {"password": pwd, "username": name}
        login_resp = request.post_request(url="http://qa.guoyasoft.com:8099/admin/login", json=login_data)
        assertions.assert_code(login_resp.status_code, 200)
        login_resp_json = login_resp.json()
        assertions.assert_in_text(login_resp_json['message'], msg)

















