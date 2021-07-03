# 切片可以获取一段数据，下标（索引只能获取一个数据）
# 切片语法：变量[start: end: step]，切片后会得到一个新的字符串
# start 开始位置的下标
# end   结束位置的下标，不包含end对应的下标的字符，默认是len()
# step  步长，下标之间的间隔，默认是1
"""
正数下标：  0  1  2  3  4
字符串：    a  b  c  d  e
负数下标： -5 -4 -3 -2 -1
"""

my_str = 'abcde'
my_str1 = my_str[0:4:2]
print(my_str1)  # ac

# step 如果是1，即默认值，可以省略
my_str2 = my_str[2:4]
print(my_str2)  # cd

# end 位置省略，表示是len()，即可以取到最后一个元素，冒号保留，前提step 是正数
my_str3 = my_str[2::]
print(my_str3)  # cde

# end 位置省略，step 为负数，则end 表示可以取到第一个元素，冒号保留
my_str3 = my_str[2::-1]
print(my_str3)  # cba

# start 位置也可以省略，表示是0，即第一个元素，冒号保留
my_str4 = my_str[:3]  # abc
print(my_str4)

# 【最常用】start 和 end 都省略，但是冒号保留一个，得到和本身一样的字符串
my_str5 = my_str[:]  # abcde
print(my_str5)

print(my_str[-4:-1])  # bcd
print(my_str[3: 1], '没有数据')  # 没有数据

# 步长可以是负数
print(my_str[3:1:-1])  # dc

# 【最常用】字符串的逆置，只保留步长需要两个冒号占位 start 和 end
print(my_str[::-1])  # edcba

# my_str[0:5:2]
print(my_str[::2])  # ace

# start 开始位置能否通过 step 步长 达到 end 结束位置，不能达到就没有数据
print(my_str[1:4:-1], '没有数据')
