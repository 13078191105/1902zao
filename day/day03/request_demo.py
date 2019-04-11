
import requests
def cc_dom():
    data = {"username":"admin","password":"123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)

    text_body = response.text
    print(type(text_body))
    print(text_body)
    
    json_body = response.json()
    print(type(json_body))
    print(json_body)
    assert 200 == response.status_code
    assert '成功' in json_body['message']

    assert 200 == json_body ['code']

    data_dict = json_body['data']
    token_head_ = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization':token_head_+' '+token_}

    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    print(get_info.text)
    assert 200 == json_body['code']
    get = requests.get(url='http://192.168.60.132:8080/product/list?pageNum=1&pageSize=1', headers=head)
    print(get.text)
    print(get.text)
    json = get.json()
    json_data_ = json['data']
    list_ = json_data_['list']
    for i in list_:
        print(i)



if __name__ == '__main__':
    cc_dom()
    pass



