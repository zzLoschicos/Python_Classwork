# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/4 21:25
@software: PyCharm
"""
#2. 给定任意奇数个整数，要求计算中间数（数值大小处于中间得数）并输出。
a = 1
qlist = []
while a:
    q = input("请输入奇数个整数(用逗号分开):").rstrip()
    qlist = q.split(",")
    print(qlist)
    qlist = [int(qlist[i]) for i in range(len(qlist))]
    if int(len(qlist)) % 2 == 1:  # 检测输入的是否为奇数个并且是否为整数
        a = 0
    else:
        continue
qlist.sort()  # 排序
print("a=%s" % qlist[int(len(qlist) / 2)])  # 下角标的数
