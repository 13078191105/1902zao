



#try except 用来捕捉异常
if __name__ == '__main__':
    a= "123456"
    #try 用于异常处理；如果出现异常则执行except 内的代码
    try:
        #判断 啊是否包含5
        assert '9'in a
    #exce 报错后执行
    except:
        print('a里没有')
    #不管 是否有异常，finally 里面的代码 都会被执行
    finally:
        print('最后..........')


    pass