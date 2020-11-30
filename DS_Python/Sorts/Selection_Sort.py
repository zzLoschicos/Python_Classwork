# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@contact: 13210707427@163.com
@datetime:2020/11/30 10:05
@software: PyCharm
"""
"""
选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，所以称为：选择排序。
1、原理
　　设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素找到最小的元素，将它和第一个元素互换
　重复上述操作，我们找出第二小的元素和第二个位置的元素互换，以此类推找出剩余最小元素将它换到前面，即完成排序
"""


def select_sort(array):
    # 第一层for表示循环选择的遍数
    for i in range(len(array)-1):
        # 将起始元素设成最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                # 如果当前元素比最小元素小，则把当前元素的角标记为最小元素的角标
                min_index = j
            # 查找一遍后，将最小元素与起始元素互换
        array[min_index], array[i] = array[i], array[min_index]
    return array


if __name__ == '__main__':
    # array = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
    # print(select_sort(array))
    print(select_sort([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]))