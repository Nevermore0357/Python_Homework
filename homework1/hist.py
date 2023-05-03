'''
使用直方图统计一个数据集出现的频率
'''
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

df = pd.read_excel('stock.xlsx')
data1 = df['price2']
data2 = df['price3']
# hist只能传一维列表进去
plt.hist([data1, data2], bins=10, edgecolor='black', alpha=0.7, rwidth=1, label=['4月14','4月15'])

# 添加标题和标签
plt.title('Stock Price')
plt.xlabel('Price($)')
plt.ylabel('Frequency')

# 显示图形
plt.legend()
plt.show()


# std_dev = np.std(data)
