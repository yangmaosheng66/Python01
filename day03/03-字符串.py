# 单引号
name = 'isaac'
print(type(name),name)
# 双引号
name = "isaac"
print(type(name), name)
# 三（单/双）引号
my_str1 = """hello world
hello python!
"""

print(type(my_str1), name)

my_str = '''aaa
bbb
'''

print(type(my_str), name)

# 如果字符串本身包含单引号，使用双引号定义，如果包含双引号，可以使用单引号定义，或者统一使用三单/双引号定义
# my name is 'isaac'
my_name = "my name is 'isaac'"

# 在python中，字符串可以乘上一个整数（包括0），代表重复整数个该字符串
my_str = 'hello' * 0
print(type(my_str), my_str)
