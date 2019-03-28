def jiafa_dmo():
    a = 5
    b = 4
    add = a + b
    print(add)


def pingjie_demo():
    a = 'world'
    b = 250
    print('%s %s ' % (a, b))


def pingjie2_demo():
    a = 'hdhdh'
    b = 'hdhdhd'
    a_b = a + b
    return a_b


if __name__ == '__main__':

    list=[1,5,7,4,5,4,14,5,4,5]
# print(list[0])
# print(list[-1])
# list[-1]=2
# print(list)
# print(list.pop())
# print(list)
# d = {'name': 'ysl', 'pwd': '123456'}
# print(d.pop('name'))
# print(d)
# for i in range(5):
#     print('hello world')
# alist = [1,2,3,4,5,6]
# for i in range(4):
#     print(alist[i])
# for i in alist:
#     print(i)
# str = '经济活动覅多会发货'
# assert '经'in str
# a = 2
# b = 3
# if a > b:
#     print('a= 2')
# else:
#     print('b= 3')
#     a = 0
# print('hhhhhhhh')
# a += 1
#     try:
#         assert '1'not in list
#     except:
#         print('没有')
#     finally:
#         print('----------')
#     pass
    for i in range(5):
        print(i)
        if i == 3:
            continue
        print('第%s次循环'%i)