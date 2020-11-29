# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@contact: 13210707427@163.com
@datetime:2020/11/29 14:32
@software: PyCharm
"""
"""
第6章函数-6 缩写词 (20分)
缩写词是由一个短语中每个单词的第一个字母组成，均为大写。
例如，CPU是短语“central processing unit”的缩写。
函数接口定义：
acronym(phrase);
phrase是短语参数，返回短语的缩写词
裁判测试程序样例：
/* 请在这里填写答案 */
phrase=input()
print(acronym(phrase))
输入样例：
central  processing  unit
输出样例：
CPU
"""


def acronym(phrase):
    str1 = ""  # 用于存储
    str = list(phrase.split())  # 用空格分割，将每一个元素都放在list集合中；
    for i in str:  # 临时变量ｉ用于获取集合str中的元素对象
        for j in i:  # 遍历ｉ中的字符元素，j遍历元素对象i
            if j.isupper():  # isupper() 用来判断这个字符是否是大写的英文字母
                str1 = str1 + j  # 如果是大写的英文字母，就把这个字符加到str1 这个字符串中
                break  # 结束循环，只取第一个字符
            elif j.islower():  # islower() 用来判断这个字符是否是小写的英文字母
                str1 = str1 + j.upper()  # upper()是将这个小写字母转化为大写字母 然后加到str1这个字符串中
                break  # 结束循环，只取第一个字符
    return str1  # 返回str1字符串


if __name__ == '__main__':
    phrase = input()
    print(acronym(phrase))
