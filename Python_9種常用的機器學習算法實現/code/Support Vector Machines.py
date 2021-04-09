
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# SVM
from sklearn import svm
# 1. 准备数据
svm_X_train, svm_y_train = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1, n_classes=4)
# 2. 构造训练与测试集
l, r = svm_X_train[:, 0].min() - 1, svm_X_train[:, 0].max() + 1
b, t = svm_X_train[:, 1].min() - 1,svm_X_train[:, 1].max() + 1
n = 1000
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
svm_X_test = np.column_stack((grid_x.ravel(), grid_y.ravel()))
# 3. 训练模型
# svm_model = RandomForestClassifier(max_depth=4)
svm_model = svm.SVC(kernel='rbf', gamma=1, C=0.0001).fit(svm_X_train, svm_y_train)
svm_model.fit(svm_X_train, svm_y_train)
# 4. 预测数据
svm_y_pred = svm_model.predict(svm_X_test)
# 5. 可视化
grid_z = svm_y_pred.reshape(grid_x.shape)
plt.figure('SVM')
plt.title('SVM')
plt.pcolormesh(grid_x, grid_y, grid_z, cmap='Blues')
plt.scatter(svm_X_train[:, 0], svm_X_train[:, 1], s=30, c=svm_y_train, cmap='pink')
plt.show()