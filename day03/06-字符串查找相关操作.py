# find() 在字符串中查找是否存在某个字符串
# my_str.find(sub_str, start, end)
# sub_str: 要在字符串中查找的内容，类型 str
# start： 开始位置，从哪里开始查找，默认是0
# end: 结束的位置，查找到哪里结束，默认是len()
# 返回值：即方法执行的结果是什么，如果找到 sub_str，返回 sub_str 在 my_str 中的正数下标
# 如果没有找到，返回 -1
my_str = 'hello world python and hi python'

index = my_str.find('hello')  # 0
print(index)

# 从下标为3的位置，开始查找字符串 hello
print(my_str.find('hello', 3))  # -1 没有找到
print(my_str.find('python'))  # 12
print(my_str.find('python', 15))  # 26

# rfind() 从右边（从后往前）开始查找，但仍然返回正数下标
print(my_str.rfind('python'))  # 26

# i() 在字符串中查找是否存在某个字符串
# my_str.i(sub_str, start, end)
# sub_str: 要在字符串中查找的内容，类型 str
# start： 开始位置，从哪里开始查找，默认是0
# end: 结束的位置，查找到哪里结束，默认是len()
# 返回值：即方法执行的结果是什么，如果找到 sub_str，返回 sub_str 在 my_str 中的正数下标
# 【和find的唯一区别】如果没有找到，i 会报错

print(my_str.index('hello'))  # 0

# print(my_str.i('hello', 5))  # substring没有找到，报错

# rindex() 从右边（从后往前）开始查找，但仍然返回正数下标
print(my_str.rindex('python'))  # 26

# count(sub_str, start, end) 统计所查找字符串出现的次数
print(my_str.count('aaa'))  # 0
print(my_str.count('hello'))  # 1
print(my_str.count('python'))  # 2
print(my_str.count('python', 20))  # 1
