'''
从excel读取两列数据，生成折线图
'''
import pandas as pd
import matplotlib.pyplot as plt

#设置绘图风格
plt.style.use('ggplot')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
wechat = pd.read_excel('stock.xlsx')
# 绘制单条折线图
plt.plot(wechat.date2, # x轴数据
         wechat.price2, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 1.5, # 折线宽度
         color = 'steelblue', # 折线颜色
         label = 'A股票',
         # marker = 'o', # 折线图中添加圆点
         # markersize = 6, # 点的大小
         # markeredgecolor='black', # 点的边框色
         # markerfacecolor='brown', # 点的填充色
         )
plt.plot(wechat.date2, # x轴数据
         wechat.price3, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 1.5, # 折线宽度
         color = 'indianred', # 折线颜色
         label = 'B股票',
         )
#对于X轴，只显示x中各个数对应的刻度值
plt.xticks(fontsize=8, )  #改变x轴文字值的文字大小
# 添加x,y轴标签
plt.xlabel('日期')
plt.ylabel('价格')
# 添加图形标题
plt.title('股票价格')
plt.legend()
# 显示图形
plt.show()
