import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

#保存数据，可用于之后的学习研究
def save_data(data, path):
    Note=open(path,mode='w')
    print("保存数据")
    Note.write(str(data))
    Note.close()

#读取xls文件数据
def read_excel(excel_name,list):
    """参数：
    输入：excel的名字
    输出：目标表的名字"""
    df = pd.read_excel(excel_name)
    df_new = df[list]

    return df_new

# def read_excel(excel_name,sheet_name):
#     """参数：
#     输入：excel的名字
#     输出：目标表的名字"""
#     workbook = xlrd.open_workbook(excel_name)  #打开文件
#     sheet = workbook.sheet_by_name(sheet_name)  #读取sheet页
#     # 获取表的行列数
#     rows = sheet.nrows
#     cols = sheet.ncols
#     all_data = []
#     tempList = []
#     # 读取放置在excel中的数据
#     for col in range(3, 13):
#         for row in range(1, rows):
#             print(rows)
#             tempList.append(sheet.cell(row, col).value)
#         all_data.append(tempList)
#         tempList = []
#     return all_data

#设置盒图的图片参数
def draw_box(all_data):
    fig = plt.figure(figsize=(40, 15))  # 设置画布大小
    ax = fig.add_subplot(111)  # 图形在画布中的布局
    ax.set_title("Stock Price", fontsize=24)  # 以下表示设置坐标标签以及字体大小
    # ax.set_xlabel('', fontsize=22)
    ax.set_ylabel('price', fontsize=22)
    boxprops = dict(facecolor='lightblue', edgecolor='black', linewidth=2, linestyle='--')
    all_data.boxplot(ax=ax, fontsize=24,patch_artist=True,boxprops=boxprops)

    plt.show()
    pd.set_option('display.max_columns', None)  # 为了将数据全部展示，显示全部列


if __name__ == '__main__':
    list1=['data0','data1','data2','data3']
    all_data = read_excel('stock.xlsx',list1) #读取数据，参数1是excel的名字，参数2是里面具体的表名
    draw_box(all_data)#绘制图表

