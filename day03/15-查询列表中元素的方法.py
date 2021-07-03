my_list = [1, 3.14, 'isaac', True]
# i() 根据数据值，查找元素所在的下标，找到返回元素的下标，没有找到，程序报错
# 列表中没有find() 方法，只有index() 方法
# 查找元素3.14 在列表中的下标
print(my_list.index(3.14))  # 1

# print(my_list.i(100))  # 程序报错，因为元素100 不存在


# count() 统计元素出现的次数
print(my_list.count(1))  # 2 True会被当成数字1

# in /not in 判断元素是否存在，一般和if 结合使用
print(3.14 in my_list)  # True
print(3.14 not in my_list)  # False
