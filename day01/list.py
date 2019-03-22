alist = [1, 14, 477, 45, 4154, 45744, 447, 1, 85, 74, 1]


def list_demo():
    print(alist)


def list_update():
    alist[0] = 5
    print(alist)


def str_demo():
    a = 'world'
    b = 250


def orderBy_demo():
    print('正序排列')
    sort_demo()
    print('倒序排列')
    reverse_demo()
    pass


def sort_demo():
    alist.sort()
    print(alist)


def reverse_demo():
    alist.reverse()
    print(alist)


if __name__ == '__main__':
    # list_demo()
    # list_update()
    # str_demo()
    # print(len(alist))
    # print(alist.pop())
    # print(alist)
    # alist.pop(4)
    # print(alist)
    orderBy_demo()

    pass
