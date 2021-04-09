import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# PCA
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# 1. 准备数据
pca_data=load_iris()
pca_X_data=pca_data.data
pca_y_data=pca_data.target
# 2. 训练模型, 维度为2
pca_model=PCA(n_components=2)  
# 3. 降维
reduced_X=pca_model.fit_transform(pca_X_data)
# 4. 可视化
red_x,red_y=[],[]
blue_x,blue_y=[],[]
green_x,green_y=[],[]

for i in range(len(reduced_X)):
 if pca_y_data[i] ==0:
  red_x.append(reduced_X[i][0])
  red_y.append(reduced_X[i][1])
 elif pca_y_data[i]==1:
  blue_x.append(reduced_X[i][0])
  blue_y.append(reduced_X[i][1])
 else:
  green_x.append(reduced_X[i][0])
  green_y.append(reduced_X[i][1])

plt.figure('PCA')
plt.title('PCA')
plt.scatter(red_x,red_y,c='r')
plt.scatter(blue_x,blue_y,c='b')
plt.scatter(green_x,green_y,c='g')
plt.show()