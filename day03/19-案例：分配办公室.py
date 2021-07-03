import random

# 定义办公室列表
office_list = [[], [], []]  # 三个小列表就是三个办公室，对应的下标 0, 1, 2

# 定义老师列表
teacher_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for i in teacher_list:
    # 老师逐个抓阄
    office_num = random.randint(0, 2)
    # 把抓过阄的老师添加进相应的办公室子列表中
    office_list[office_num].append(i)

# 打印办公室列表
print(office_list)

# 打印每个办公室中的老师
for j in office_list:
    print(f'{office_list.index(j) + 1}号办公室的老师有{len(j)}个，分别是：', end='')
    for t in j:
        print(t, end='')
    print()
