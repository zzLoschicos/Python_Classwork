# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/13 21:33
@software: PyCharm
"""
"""
利用集合分析活动投票情况。第一小队有五名队员，序号是1,2,3,4,5;
第二小队也有五名队员，序号6,7,8,9,10。
输入一个得票字符串，求第二小队没有得票的队员
"""
str1 = input().split(",")
str2 = [6, 7, 8, 9, 10]
flag = 0
list = []
for i in str2:
    flag = 0
    for j in str1:
        if i == int(j):
            flag = 1
            break
    if flag == 0:
        list.append(i)
for i in range(0,len(list)):
    print(f"{list[i]}", end=" ")
    if i < len(list) - 1:
        print(" ", end="")
exit(0)