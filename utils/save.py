'''
生成一列数据并保存在指定excel，会覆盖原excel数据
'''
import numpy as np
import pandas as pd

# 生成16个范围在3到4之间的两位小数
data = np.random.uniform(low=3.0, high=4.0, size=(16,))
data = np.around(data, decimals=2)

# 将新数据存入DataFrame对象
df = pd.DataFrame({'price3': data})

# 将DataFrame对象写入Excel表格中
writer = pd.ExcelWriter('D:\python\Py_MySQL\homework1\stock.xlsx',engine='openpyxl')
df.to_excel(writer,index=False)
writer.save()
