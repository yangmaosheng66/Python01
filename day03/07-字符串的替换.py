# my_str.replace(old_str, new_str, count) 字符串的替换，将my_str 中的old_str 替换成new_str
# old_str: 将要被替换的字符串
# new_str: 替换成的新字符串
# count: 替换的次数，默认全部替换
# 返回值：得到一个新的字符串，不会改变原来的字符串
my_str = 'hello world python and hi python'

my_str1 = my_str.replace('python', 'java')
print('my_str :', my_str)
print('my_str1:', my_str1)

my_str2 = my_str.replace('python', 'java', 1)  # 替换一次
print('my_str2:', my_str2)
