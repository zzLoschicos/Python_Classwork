# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@contact: 13210707427@163.com
@datetime:2020/11/30 9:00
@software: PyCharm
"""
"""
冒泡排序
0.如果遇到相等的值不进行交换，那这种排序方式是稳定的排序方式。
1.原理：比较两个相邻的元素，将值大的元素交换到右边
2.思路：依次比较相邻的两个数，将比较小的数放在前面，比较大的数放在后面。
　　　　(1)第一次比较：首先比较第一和第二个数，将小数放在前面，将大数放在后面。
　　　　(2)比较第2和第3个数，将小数 放在前面，大数放在后面。
　　　　......
　　　　(3)如此继续，知道比较到最后的两个数，将小数放在前面，大数放在后面，重复步骤，直至全部排序完成
　　　　(4)在上面一趟比较完成后，最后一个数一定是数组中最大的一个数，所以在比较第二趟的时候，最后一个数是不参加比较的。
　　　　(5)在第二趟比较完成后，倒数第二个数也一定是数组中倒数第二大数，所以在第三趟的比较中，最后两个数是不参与比较的。
　　　　(6)依次类推，每一趟比较次数减少依次。
"""


def bubble_sort(array):
    for i in range(1, len(array)): # array[i] 遍历列表中的元素
        for j in range(0, len(array) - i):  # array[j] 遍历一轮排序结束后的元素
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 48, 15, 5, 36, 21]
    print(bubble_sort(array))
