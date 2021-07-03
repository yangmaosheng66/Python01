my_str = 'hello world python and hi python'
my_str1 = 'HELLO world PYTHON and HI python'

# capitalize()
# 把字符串中的第一个字符大写
print(my_str.capitalize())

# title()
# 把字符串中的每一个单词首字母大写
print(my_str.title())

# upper()
# 把字符串中的每一个字母大写
print(my_str.upper())

# lower()
# 把字符串中的每一个字母小写
print(my_str1.lower())

# islower()
# 判断字符串中的每一个字母是否都是小写，返回bool
print(my_str1.islower())  # False

# startswith(obj)
# 判断字符串是否以某个字符串（区分大小写）开头，返回bool，
print(my_str.startswith('hello'))  # True
print(my_str.startswith('HELLO'))  # False

# endswith(obj)
# 判断字符串是否以某个字符串（区分大小写）结尾，返回bool，
print(my_str.endswith('python'))  # True
print(my_str.endswith('PYTHON'))  # False

# ljust(width)
# 返回一个原字符串左对齐，并使用空格填充至长度width的新字符串（一个空格为width = 2）
print('hello'.ljust(10), '!')

# rjust(width)
# 返回一个原字符串右对齐，并使用空格填充至长度width的新字符串（一个空格为width = 2）
print('hello'.rjust(10), '!')

# center(width)
# 返回一个原字符串居中，并使用空格填充至长度width的新字符串，width为字符串左右空格长度之和（一个空格为width = 2）
print('hello'.center(10), '!')

# lstrip()
# 删除原字符串开头的空白字符
print('     hello'.lstrip())

# rstrip()
# 删除原字符串末尾的空白字符
print('hello     '.rstrip(), '!')

# strip()
# 删除原字符串开头和末尾的空白字符
print('     hello     '.strip(), '!')

# partition(str)
# 把原字符串从左到右的第一个str 以str 分割成三部分，str 前，str 和str 后，返回值为元组
print('hello'.partition('l'))
print(type('hello'.partition('l')))

# rpartition(str)
# 把原字符串从右到左的第一个str 以str 分割成三部分，str 前，str 和str 后，返回值为元组
print('hello'.rpartition('l'))
print(type('hello'.rpartition('l')))

# splitlines()
# 按照行分隔，返回一个包含各行作为元素的列表
print('Hello\nWorld')
print('Hello\nWorld'.splitlines())

# isalpha()
# 判断字符串中的所有字符是否都是字母（包括汉字，不包括空格），返回bool
print('Hello'.isalpha())  # True
print('Hello你好'.isalpha())  # True
print('He11o'.isalpha())  # False

# isdigit()
# 判断字符串中的所有字符是否都是数字（0123456789，不包括负号小数点空格）返回bool
print('443'.isdigit())  # True
print('443kid'.isdigit())  # False

# isalnum()
# 判断字符串中的所有字符是否都是字母或数字（包括汉字，不包括空格），返回bool
print('443kid'.isalnum())  # True
print('443是kid'.isalnum())  # True
print('443 kid'.isalnum())  # False

# isspace()
# 判断字符串中的所有字符是否只有空格（空字符串不是空格），返回bool
print('         '.isspace())  # True
print('h e l l o'.isspace())  # False
print(''.isspace())  # False
