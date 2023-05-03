'''
使用直方图生成日期和价格对应的图像，
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('stock.xlsx')
df['date1'] = df['date1'].astype(str)
data1 = df['price1']
data2 = df['date1']

plt.bar(data2,data1,width=0.5)
plt.show()