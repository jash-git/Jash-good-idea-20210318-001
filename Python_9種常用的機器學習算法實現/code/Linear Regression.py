import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Linear Regression 一元回归
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# 1. 准备数据
lr_X_data, lr_y_data = datasets.make_regression(n_samples=500,n_features=1,n_targets=1,noise=2) # feature为1维度
# 2. 构造训练与测试集
lr_X_train, lr_X_test, lr_y_train, lr_y_test = train_test_split(lr_X_data, lr_y_data, test_size=0.3)
# 3. 训练模型
lr_model = linear_model.LinearRegression()
lr_model.fit(lr_X_train, lr_y_train)
# 4. 预测数据
lr_y_pred = lr_model.predict(lr_X_test)
# 5. 评估模型
lr_mse = mean_squared_error(lr_y_test, lr_y_pred)
print("mse:", lr_mse)
# 6. 可视化
plt.figure('Linear Regression')
plt.title('Linear Regression')
plt.scatter(lr_X_test, lr_y_test, color='lavender', marker='o')
plt.plot(lr_X_test, lr_y_pred, color='pink', linewidth=3)
plt.show()

# print info mse: 4.131366697554779