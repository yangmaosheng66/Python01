# my_str.join(可迭代对象)
# 可迭代对象可以是str，列表（需要列表中的每一个数据都是字符串类型），元组
# 将my_str这个字符串添加到可迭代对象的两个元素之间
# 返回值：一个新的字符串，不会改变原字符串的值

my_str = '_'.join('hello')  # 会把'_' 加入到'hello' 每两个元素直接
print(my_str)  # h_e_l_l_o

print('_*_'.join('hello'))  # h_*_e_*_l_*_l_*_o

# 定义列表
my_list = ['hello', 'world', 'python']

print('_'.join(my_list))  # hello_world_python
print(' '.join(my_list))  # hello world python
