# 下标也称为是索引，是一个整型数字，可以是正/负数
# 正数下标从0开始，表示第一个字符，负数下标 -1 表示最后一个字符
"""
正数下标： 0  1  2  3  4
字符串：   h  e  l  l  o
负数下标： -5 -4 -3 -2 -1
"""

my_str = 'hello'
# 下标的使用语法     变量[下标]
print(my_str[0])
print(my_str[1])

print(my_str[-1])
print(my_str[-3])

# len() 函数可以得到字符串的长度
print(len(my_str))
# 使用正数下标书写字符串中最后一个元素
print(my_str[len(my_str)-1])
