# 操场跑圈 一共需要跑5圈
# 每跑一圈,需要做3个俯卧撑,

# 1. 定义变量记录跑的圈数
i = 0

while i < 5:
    # 2. 定义变量, 记录每一圈做了多少个俯卧撑
    j = 0  # 每次进入内层循环，都要重置俯卧撑计数
    # 3. 操场跑圈
    print('操场跑圈中.....')
    # 4. 做俯卧撑
    while j < 3:
        print('做了一个俯卧撑')
        j += 1
    # 一圈完整了,圈数加1
    i += 1
