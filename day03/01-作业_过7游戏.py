# 判断一个正整数是否是7的倍数或包含7
print('# 判断一个正整数是否是7的倍数或包含7\n')
num = int(input('请输入一个正整数：'))

for i in range(1, num + 1):
    if i % 7 == 0:
        print(i)
    else:
        for j in str(i):
            if j == '7':
                print(i)
                break
        else:
            print('过', i)
