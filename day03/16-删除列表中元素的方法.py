my_list = [1, 2, 3, 4, 5]
print(my_list, '原列表')

# 1. remove(元素值) 根据元素的值删除，直接删除原列表中的元素，没有返回值
my_list.remove(4)
print(my_list)
# my_list.remove(4)  # 要删除的元素不存在，程序报错


# 2. 根据元素的下标删除
# 2.1 pop(下标) 不写下标默认删除最后一个元素，返回值为删除的内容
print(my_list.pop())  # 删除最后一个元素5
print(my_list)
print(my_list.pop(2))  # 删除下标为2的元素3
print(my_list)
# print(my_list.pop(10))  # 删除的下标越界，程序报错

# 2.2 del 列表[下标]
del my_list[1]  # 删除下标为1 的元素2
print(my_list)



