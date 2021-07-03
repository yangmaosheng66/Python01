# 输入一个正整数，判断是否为素数（只能被1和本身整除）
print('# 输入一个正整数，判断是否为素数（只能被1和本身整除）\n')
num = int(input('请输入一个正整数：'))

for i in range(2, num):
    if num % i == 0:
        print(f'{num}不是素数，可以被{i}整除')
        break
else:
    print(num, '是素数')
