'''
主成分分析散点图
https://github.com/ZJUEarthData/DS_explore.git
'''
import sys
import os
import sklearn
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_excel("dataset.xlsx",engine='openpyxl')
X = df.drop("TRUE VALUE", axis=1)

# 真实分类信息的列
labels = df["TRUE VALUE"]

# print(X)
# X.info()

# 原数据集的真实分类信息
tag = list(np.unique(labels))
#print(tag)
variable = X.columns
# print(variable)

# 降维前先需要对数据进行标准化处理
scaler = StandardScaler()
X_processed = pd.DataFrame(scaler.fit_transform(X))

# PCA假定以原点为中心，会自动将数据集中心化处理
pca1 = PCA(n_components=2)
# 将数据降至2维
X_reduced1 = pca1.fit_transform(X_processed)
# X_reduced1.shape=(2272,2)



def biplot(reduced_data, labels, pc, variable):
    """
    plot componential biplot for two principle components

    :param reduced_data: data processed by PCA
    :param labels: labels of original dataset
    :param pc: all the principle components
    :param variable: the name of the variables of the data set
    """
    plt.figure(1, figsize=(14, 10))

    legend = []  #
    classes = np.unique(labels)  # label type
    n = pc.shape[1]
    # colors = ['g', 'r', 'y']
    # markers = ['o', '^', 'x']

    x = reduced_data[:, 0]  # variable contributions for PC1
    y = reduced_data[:, 1]  # variable contributions for PC2
    scalex = 1.0 / (x.max() - x.min())
    scaley = 1.0 / (y.max() - y.min())

    # Draw a data point projection plot that is projected to
    # a two-dimensional plane using normal PCA
    for i, label in enumerate(classes):
        plt.scatter(x[labels == label] * scalex,
                    y[labels == label] * scaley,
                    linewidth=0.01)
        # hyperparameter in plt.scatter(): c=colors[i], marker=markers[i]
        legend.append("Label: {}".format(label))

    plt.legend(legend)

    # plot arrows as the variable contribution,
    # each variable has a score for PC1 and for PC2 respectively
    for i in range(n):
        plt.arrow(0, 0, pc[0, i], pc[1, i], color='k', alpha=0.7,
                  linewidth=1, )
        plt.text(pc[0, i] * 1.01, pc[1, i] * 1.01, variable[i],
                 ha='center', va='center', color='k', fontsize=12)

    plt.xlabel("$PC1$")
    plt.ylabel("$PC2$")
    plt.title("Componential biplot")
    plt.grid()
    plt.show()
biplot(X_reduced1, labels, pca1.components_, variable)