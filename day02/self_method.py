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



if __name__ == '__main__':
    # for i in range(5):
    #     print('hello world')
    #     for j in range(2):
    #         print('耶耶耶')

    # for i in range(1,10):
    #     for j in range(1,i+1):
    #         print('%s x %s = %s '%(i,j,i*j),end=' ')
    #     print('')
    cfkjb_bianli()

    pass




