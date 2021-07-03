# code=utf-8
import os
import math
import pandas as pd

# 指定行数拆分写入新工作簿
# 打开文件，在单引号里面输入要拆分的文件的目录，默认为csv，要拆分的文件需要有一行表头
# 表格第一列为手机号，第二列为姓名
url = r'C:\Users\yangm\Desktop\20210614发短信\20210614发短信.csv'
# 在等号后面输入拆分后每个表格的行数
row_num_result = 10
# 输入要拆分的列的范围，默认为第1列至第2列
start = 1
end = 2
# 输入姓名左右两边的短信文本，注意不要漏标点符号
left_text = '尊敬的客户'
right_text = '，诚邀您参加'

# 读取源文件
df = pd.read_csv(url, dtype=str, sep=',')
# 读取行数（不含表头）
row_num_total = df.shape[0]

# 每个excel保存row_num_single行
for i in range(0, row_num_total):
    # 在单引号内修改短信文本（两个+中间的变量为姓名）
    df.iloc[i, 1] = '%s%s%s' % (left_text, df.values[i][1], right_text)

for i in range(0, math.ceil(row_num_total / row_num_result)):
    save_data = df.iloc[i * row_num_result: (i + 1) * row_num_result, start - 1:2]
    # 保存文件路径以及文件名称，默认为被拆分表格所在的目录
    file_name = os.path.splitext(url)[0] + '（第' + str(i+1) + '次拆分）' + '.xlsx'
    # 保存格式为.csv，如果是xlsx则修改为save_data.to_excel，如果是csv则修改为save_data.to_csv
    save_data.to_excel(file_name, index=False, header=None)

# 输出结果
print('# 指定行数拆分写入新工作簿')
print(f'拆分成功！原表格不含表头有{row_num_total}行，按每{row_num_result}行一个表格拆分，共拆分出{i+1}个表格')
