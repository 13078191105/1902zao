# class 类
# object 对象|或者所有类的父类
# 声明类的语法：class ： 就是声明一个类；human：类的名字；（）；括号里面填 这个的父类
class human(object):
    # 类的初始化方法 self：就代表类 本身
    def __init__(self,name,age,sex):
        # 将入参的name 赋值类 类本身的name
        self.name = name
        self.age = age
        self.sex = sex
    # 类里面方法 必传self
    def myInfo(self):
        print('我叫%s,我今年%s岁，%s'%(self.name,self.age,self.sex))
    def myInfoStr(self):
        return '我叫%s,我今年%s岁，%s'%(self.name,self.age,self.sex)
class Tester(human):

    def zhiXingCeShi(self):
        # 调用了父类的属性
        print(self.name)
        print('我在执行测试，别打扰我')
        # 调用父类的方法
        self.myInfo()




if __name__ == '__main__':
    # = 后面调用了这个类 传入参数，参数必传，而且完整
    # = 前面是对象名
    # 对象是类的实例化
    # human = human('刘智',23,'女')
    # print(type(human))
    # 对象可使用 类中的方法
    # human.myInfo()
    # human.myInfoStr()
    tester = Tester('lz', 23, '女')
    tester.zhiXingCeShi()