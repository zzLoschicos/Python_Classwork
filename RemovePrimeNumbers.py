# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/4 22:16
@software: PyCharm
"""
# 4、编写程序，删除列表中的所有素数。
i = input("请输入一段数字,并用空格隔开：").rstrip().split(" ")
i_list = list(i)
b_list = []
f_list = []
for ints in i_list:
    s = int(ints)
    f_list.append(s)
    for i in range(2, s):
        if s % i == 0:
            break
        if i == s - 1:
            b_list.append(s)
print(f_list)
for ss in b_list:
    while ss in f_list:
        f_list.remove(ss)
print(f_list)
