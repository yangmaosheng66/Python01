# 向列表中添加元素的方法，都是直接在原列表中进行添加的，不会返回新的列表
my_list = ['德玛西亚', '德克萨斯', '艾欧尼亚', '比尔吉沃特']
print(my_list)

# 列表.append(元素) 向列表的尾部追加元素
result = my_list.append('暗影岛')  # append()方法没有返回值
print(result)  # None 关键字，表示空
print(my_list)

# 列表.insert(下标, 元素) 在指定的下标位置进行添加元素
my_list.insert(4, '黑色玫瑰')
print(my_list)

# 列表.extend(可迭代对象)  # str list，会将可迭代对象中的元素（字符串）逐个字符添加到原列表的末尾
my_list.extend('英雄联盟')
print(my_list)
my_list.extend(['登峰造极'])
print(my_list)
