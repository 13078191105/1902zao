#
import requests







if __name__ == '__main__':
    # 声明login_data 变量名  用来存 登录的请求数据
    data ={"username":"admin","password":"123456"}
    # = 后面就是发起一个请求，使用requesets.
    login_resp = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    print(type(login_resp))
    login_resp_text = login_resp.text
    print(type(login_resp_text))
    # print(login_resp_text)
    login_resp_json = login_resp.json()
    print(login_resp_json)
    login_resp_json_data = login_resp_json['data']
    data_tokenhead = login_resp_json_data['tokenhead']
    data_token = login_resp_json_data['token']
    head = {'Authorization': data_tokenhead + data_token}
    getoder_param = {'pageNum': 1, 'pageSize': 10}
    get_order_resp = requests.get(url='http://192.168.60.132:8080/order/list', params=getoder_param)
    print(get_order_resp.json())
    


pass