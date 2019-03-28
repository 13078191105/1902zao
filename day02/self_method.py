def list_bianli():
    alist = ['a','b','c','d']
    for i in alist:
        print("--遍历")
        print(i)
        print(i+'_hello')

def cfkjb_bianli():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s x %s = %s'%(i,j,i*j),end=' ')
        print('')

def if_dom():
    a=20
    b=10
    if a>b:
        print('a')
    else:
        print('b')
def if_demo1():
    a=20
    b=10
    if a>b:
        print('b')
    else:
        print('a')
def qiuhe_demo():
    nub = 0
    for i in range (1,51):
        if i%2 == 0 :
            nub = nub+i
    print(nub)



if __name__ == '__main__':
    # for i in range(5):
    #     print('hello world')
    #     for j in range(2):
    #         print('耶耶耶')

    # for i in range(1,10):
    #     for j in range(1,i+1):
    #         print('%s x %s = %s '%(i,j,i*j),end=' ')
    #     print('')
    # cfkjb_bianli()
    # if_dom()
    # if_demo1()
    nub = 0
    for i in range (1,10):
        if i%2 == 0 :
            nub = nub+i
    print(nub)
    nu=0
    for i in range(2, 10,2):
        nu=nu+i
    print(nu)

    pass




