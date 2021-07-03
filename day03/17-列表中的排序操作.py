# 想要对列表中的元素进行排序，前提是列表中的数据类型是一样的
my_list = [1, 5, 3, 7, 9, 6]
my_list1 = [1, 5, 3, 7, 9, 6]

# 列表.sort() 直接在原列表中进行排序，无返回值
my_list.sort()  # 默认是从小到大排序，即升序
print(my_list)
my_list.sort(reverse=True)  # 通过修改参数reverse = True，进行降序
print(my_list)

# 补充：sorted(列表) 排序，不会在原列表中进行排序，会得到一个新的列表
my_list2 = sorted(my_list1)
my_list3 = sorted(my_list1, reverse=True)  # 通过修改参数reverse = True，进行降序
print(my_list1)
print(my_list2)
print(my_list3)

print('*' * 30)

# 列表的逆置，得到一个新的列表，列表中的元素可以是不同类型
my_list4 = ['a', 'b', 'c', 'd', True]
print(my_list4[::-1])

# 在原列表中直接逆置，列表.reverse()，无返回值
my_list4.reverse()
print(my_list4)
