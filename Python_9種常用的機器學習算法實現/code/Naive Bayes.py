import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Naive Bayes 任务为分类, n_classes=4
import sklearn.naive_bayes as nb
# 1. 准备数据
nb_X_train, nb_y_train = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1, n_classes=4)
# 2. 构造训练与测试集
l, r = nb_X_train[:, 0].min() - 1, nb_X_train[:, 0].max() + 1
b, t = nb_X_train[:, 1].min() - 1, nb_X_train[:, 1].max() + 1
n = 1000
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
nb_X_test = np.column_stack((grid_x.ravel(), grid_y.ravel()))
# 3. 训练模型
nb_model = nb.GaussianNB()
nb_model.fit(nb_X_train, nb_y_train)
# 4. 预测数据
nb_y_pred = nb_model.predict(nb_X_test)
# 5. 可视化
grid_z = nb_y_pred.reshape(grid_x.shape)
plt.figure('Naive Bayes')
plt.title('Naive Bayes')
plt.pcolormesh(grid_x, grid_y, grid_z, cmap='Blues')
plt.scatter(nb_X_train[:, 0], nb_X_train[:, 1], s=30, c=nb_y_train, cmap='pink')
plt.show()