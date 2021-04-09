
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
# 1. 准备数据
dt_X_train, dt_y_train = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1, n_classes=4)
# 2. 构造训练与测试集
l, r = dt_X_train[:, 0].min() - 1, dt_X_train[:, 0].max() + 1
b, t = dt_X_train[:, 1].min() - 1, dt_X_train[:, 1].max() + 1
n = 1000
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
dt_X_test = np.column_stack((grid_x.ravel(), grid_y.ravel()))
# 3. 训练模型
dt_model = DecisionTreeClassifier(max_depth=4)
dt_model.fit(dt_X_train, dt_y_train)
# 4. 预测数据
dt_y_pred = dt_model.predict(dt_X_test)
# 5. 可视化
grid_z = dt_y_pred.reshape(grid_x.shape)
plt.figure('Decision Tree')
plt.title('Decision Tree')
plt.pcolormesh(grid_x, grid_y, grid_z, cmap='Blues')
plt.scatter(dt_X_train[:, 0], dt_X_train[:, 1], s=30, c=dt_y_train, cmap='pink')
plt.show()