# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/6 20:13
@software: PyCharm
[1,2,3,4,5,6,[1,2,3,4,5,6,7],7,8,9]
"""
a = input()
c = int(input())
b = ''.join(a)
# print(b)
num = 0
sum = 0
for i in range(0, len(b)):
    # print(i)
    if (b[i] == '['):
        # print(num, i)
        num += 1
        # print(num, i)
    elif (b[i] == ']'):
        num -= 1
        # print(num, i)
    if (c == num) and (b[i] != '[') and (b[i] != ']' and b[i] != ',' and b[i + 1].isdigit() == False):
        sum += 1
print(sum)
