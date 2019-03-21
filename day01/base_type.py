# 声明一个int_demo方法
def int_demo():
    # 声明aint变量，并赋值1
    aint = 1
    # 打印aint的类型；type（aint）：获取aint的类型
    print(aint)


# 声明一个int_demo方法
def str_demo():
    # 声明astr变量，并赋值1
    astr = '1'
    # 打印astr的值
    print(astr)
    # 打印astr的类型；type（astr）：获取astr的类型
    print(type(astr))

# 声明一个float_demo方法
def float_demo():
    # 声明astr变量，并赋值1
    afloat = 1.008
    # 打印astr的值
    print(afloat)
    # 打印astr的类型；type（afloat）：获取afloat的类型
    print(type(afloat))

def add(aint, bint):
    print(aint)
    print(bint)
    return aint + bint


def add(aint, bint):
    print(aint)
    print(bint)
    return aint - bint

# ctrl + k 提交。
if __name__ == '__main__':
    float_demo()
    # int_demo()
   # add1 = add(1, 4)
    #print(add1)
    pass
