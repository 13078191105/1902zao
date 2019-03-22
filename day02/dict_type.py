
import json
#声明一个全量 dict 变量（字典）
adict = {"name":"lz","pwd":"123456"}
#这是一个字符串  不过他是json 格式，也是字典的格式
adictstr = '{"name":"l","pwd":"abcde","1":"登录"}'






if __name__ == '__main__':
    # adict.pop('name')
    # print(adict['pwd'])
    # print(adict)
    # print(type(adict))
    # print(type(adictstr))
    # dumps = json.loads(adictstr)
    # print(type(dumps))
    # print(dumps['name'])
    # dumps = json.dumps(adict)
    # print(adict)
    loads = json.loads(adictstr)
    print(type(loads))
    dumps1 = json.dumps(loads, ensure_ascii=False)
    print(type(dumps1))
    print(adictstr)



    pass
