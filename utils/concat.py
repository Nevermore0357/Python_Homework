'''
生成一列新数据并放在原excel后新一列
'''
import numpy as np
import pandas as pd

# 生成n个范围在3到4之间的两位小数
data = np.random.uniform(low=1.0, high=6.0, size=(20,))
data = np.around(data, decimals=2)
df = pd.read_excel('D:\python\Py_MySQL\homework1\stock.xlsx')

# 将新数据存入DataFrame对象
# new_df = pd.DataFrame({'price1': data})
# 将新数据添加到现有的DataFrame对象中
# df = pd.concat([df, new_df], ignore_index=True)

# 将新数据添加到DataFrame对象中
new_col = pd.Series(data, name='data3')
df = pd.concat([df, new_col], axis=1)



# 将DataFrame对象写入Excel表格中
writer = pd.ExcelWriter('D:\python\Py_MySQL\homework1\stock.xlsx',engine='openpyxl')
df.to_excel(writer,index=False)
writer.save()
