# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@contact: 13210707427@163.com
@datetime:2020/11/25 10:50
@software: PyCharm
"""
"""
第6章函数-3 使用函数统计指定数字的个数 (20分)
本题要求实现一个统计整数中指定数字的个数的简单函数。
CountDigit(number,digit )
其中number是整数，digit为[1, 9]区间内的整数。
函数CountDigit应返回number中digit出现的次数。
函数接口定义：
在这里描述函数接口。例如：
CountDigit(number,digit ),返回digit出现的次数
"""
def CountDigit(n, d):
    str_num = str(n)
    dig_num = str(d)
    count = str_num.count(dig_num)
    return count
    # print(count)
    # pass


if __name__ == '__main__':
    number, digit = input().split()
    number = int(number)
    digit = int(digit)
    # count = CountDigit(number, digit)
    count = CountDigit(number, digit)
    print("Number of digit 2 in " + str(number) + ":", count)
