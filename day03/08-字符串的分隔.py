# my_str.split(sub_str, count) 将my_str 字符串按照sub_str 进行切割
# 即使用sub_str 把my_str 分隔成若干块，返回值不包含sub_str
# sub_str: 按照什么内容切割字符串，默认是空白字符（空格，tab键）
# count: 切割几次，默认全部切割
# 返回值：列表[]
my_str = 'hello world python and hi python'

result = my_str.split()  # 按照空白字符，全部切割，等效于.split(' ')
print(result)
print(type(result))  # list

my_str2 = 'hello world\tpython\njava'
print(my_str2)
print(my_str2.split())  # 默认以空白字符（空格，tab键 \t，换行 \n）分隔

print(my_str.split('python'))
print(my_str.split('python', 1))  # 切割一次

# rsplit(sub_str, count) 从右边开始切割
print(my_str.rsplit('python', 1))  # 从右边开始切割一次
