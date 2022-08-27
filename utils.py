# create by 敖鸥 at 2022/8/27

dict1 = {
    0: '餐饮',
    1: '购物',
    2: '娱乐',
    3: '通讯',
    4: '日用品',
    5: '学习',
    6: '其他'
}

dict2 = {v: k for k, v in dict1.items()}


def num2type(num):
    return dict1.get(num)


def type2num(name):
    return dict2.get(name)


def format_bills(result):
    for i in result:
        i['Type'] = num2type(i['Type'])
    return result
