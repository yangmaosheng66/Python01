import os

import pandas as pd

# 根据某列分组写入新工作簿
# 打开文件，在单引号里面输入要分组的文件的目录，默认为csv，要分组的文件需要有一行表头
url = r'C:\Users\yangm\Desktop\20210614发短信\20210614发短信.csv'
# 输入用于分组的表头名
head_name = '管辖行'

# 读取源文件
df = pd.read_csv(url, dtype=str, sep=',')
# 对指定列去重
group = df[head_name].unique()

print('# 根据某列分组写入新工作簿')
print(f'原表格不含表头有{df.shape[0]}行，共分了{len(group)}组，各组结果如下：')
for i in range(len(group)):
    # 获取去重后的内容
    group_name = group[i]
    # 生成文件名
    file_name = os.path.splitext(url)[0] + '（' + group_name + '）' + '.xlsx'
    # 分组写入工作簿，可修改要导出的列
    df.loc[df[head_name] == group[i]].to_excel(file_name, columns=['手机号', '姓名', '管辖行'], index=False)
    # 输出结果
    print(f'{group_name}：{len(df.loc[df[head_name] == group[i]])}条')

print('程序结束！')
