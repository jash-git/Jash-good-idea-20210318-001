
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# K-Nearest Neighbors 任务为分类, n_classes=4
from sklearn.neighbors import KNeighborsClassifier
# 1. 准备数据
knn_X_train, knn_y_train = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1, n_classes=4)
# 2. 构造训练与测试集
l, r = knn_X_train[:, 0].min() - 1, knn_X_train[:, 0].max() + 1
b, t = knn_X_train[:, 1].min() - 1, knn_X_train[:, 1].max() + 1
n = 1000
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
knn_X_test = np.column_stack((grid_x.ravel(), grid_y.ravel()))
# 3. 训练模型
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(knn_X_train, knn_y_train)
# 4. 预测数据
knn_y_pred = knn_model.predict(knn_X_test)
# 5. 可视化
grid_z = knn_y_pred.reshape(grid_x.shape)
plt.figure('K-Nearest Neighbors')
plt.title('K-Nearest Neighbors')
plt.pcolormesh(grid_x, grid_y, grid_z, cmap='Blues')
plt.scatter(knn_X_train[:, 0], knn_X_train[:, 1], s=30, c=knn_y_train, cmap='pink')
plt.show()