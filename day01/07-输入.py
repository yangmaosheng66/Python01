# 输入: 从键盘获取输入的内容,存入计算机程序中
# 在python中使用的是 input()函数
# input('给用户的提示信息'), 得到用户输入的内容, 遇到回车代表输入结束, 得到的数据都是字符串类型

# password = input()  # input() 括号中不写内容,语法不会出错,但是非常不友好,不知道要做什么事
password = input('请输入密码:')
print('你输入的密码是 %s' % password)
print(f'你输入的密码为{password}')
