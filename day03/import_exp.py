import os
def os_demo():
    #获取当前目录的路径
    getcwd = os.getcwd()
    print(getcwd)
    # 获取上级目录
    abspath = os.path.abspath('..')
    # 获取上上级目录的路径
    abspath1 = os.path.abspath('../..')
    print(abspath1)
def open_demo():
    # 相对路径../test.text
    # 绝对路径 c:\users\ysl\pycharmprojrots\myedu\test.text
    text_io = open('../test.text','r')
    # 读取第一行
    readline = text_io.readline()
    print(readline)
    # 读取所有行 返回一个list对象
    io_readlines = text_io.readlines()
    print(io_readlines)

if __name__ == '__main__':
    # 相对路径   ../tast.text
    # 绝对路径 c:\users\ysl\pycharmprojrots\myedu\test.text
    # w+ 代表读写模式，写人时会覆盖 源文档内容
    # text_io = open('test.text','w+')
    # text_io.write("heheh ")
    open_demo()

    pass