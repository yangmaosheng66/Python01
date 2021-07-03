server_name = [['艾欧尼亚', '黑色玫瑰', '班德尔城'],
               ['比尔吉沃特', '德玛西亚', '恕瑞玛'],
               ['峡谷之巅', '教育网']]

print(server_name[1])  # ['比尔吉沃特', '德玛西亚', '恕瑞玛']
print(server_name[1][1])  # 德玛西亚
print(server_name[1][1][1])  # 玛
# print(server_name[1][1][1][1])  # 单个字符没有下标，程序报错

print('*' * 30)

# 峡谷之巅
print(server_name[2][0])  # 峡谷之巅

# 遍历列表中的列表中的元素
for servers in server_name:
    for name in servers:
        print(name)
