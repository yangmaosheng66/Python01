my_str = 'hello python!'

for i in my_str:
    if i == 'p':
        print('包含p这个字符')
        # 已经判断出来包含了,是否还需要继续判断
        break
else:
    print('不包含p这个字符')

# 逐个输出一个正整数的每一位数字
num = eval(input('输入一个正整数：'))

# 判断该正整数有多少位
i = 0
while True:
    q = num // 10 ** i
    if q >= 10:
        i += 1
    else:
        print('该数字的位数为：', i + 1)
        # 逐个输出该正整数的每一位
        print('该数字的每一位是：', end='')
        while True:
            m = num // 10 ** i
            if m > 0 and i >= 0:
                n = m % 10
                i -= 1
                print(n, end=' ')
            else:
                break
        break
