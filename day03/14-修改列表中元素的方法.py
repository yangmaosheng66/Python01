# 修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改
# 定义变量A，默认有3个元素
my_list = ['德玛西亚', '德克萨斯', '艾欧尼亚']

print("-----修改之前，列表A的数据-----")
for i in my_list:
    print(i)

# 列表[下标]，修改列表中指定下标的元素
my_list[1] = '峡谷之巅'

print("-----修改之后，列表A的数据-----")
for i in my_list:
    print(i)
