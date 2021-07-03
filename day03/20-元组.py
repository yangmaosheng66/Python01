# 元组和列表非常相似，都可以存放多个数据，可以存放不同数据类型的数据
# 不同点：列表使用 [] 定义，元组使用 () 定义
# 列表中的数据可以修改，元组中的数据不能被修改

my_list = [18, 3.14, True, 'isaac']  # 列表

my_tuple = (18, 3.14, True, 'isaac')  # 元组
print(my_tuple, type(my_tuple))

# 元组支持下标和切片操作
print(my_tuple[1])  # 3.14

# 定义空元组，没有意义
my_tuple1 = ()  # 空元组
print(my_tuple1, type(my_tuple1))
my_tuple2 = tuple()  # 也是空元组

# 定义只含有一个数据元素的元组，数据元素后边，必须有一个逗号
my_tuple3 = (3)  # 3 <class 'int'>
my_tuple4 = (3,)  # (3,) <class 'tuple'>

print(my_tuple3, type(my_tuple3))
print(my_tuple4, type(my_tuple4))
