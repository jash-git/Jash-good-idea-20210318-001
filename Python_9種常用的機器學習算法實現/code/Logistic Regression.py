
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Logistic Regression 二分类
from sklearn import linear_model

# 1. 准备数据
np.random.seed(123)
logit_X_data = np.random.normal(size=1000)
logit_y_data = (logit_X_data>0).astype(np.float)
logit_X_data[logit_X_data>0]*=5
logit_X_data+=.4*np.random.normal(size=1000)
logit_X_data=logit_X_data[:,np.newaxis]
# 2. 构造训练与测试集
logit_X_train, logit_X_test, logit_y_train, logit_y_test = train_test_split(logit_X_data, logit_y_data, test_size=0.3)
# 3. 训练模型
logit_model=linear_model.LogisticRegression(C=1e4) #classifier
logit_model.fit(logit_X_train,logit_y_train)
# 4. 预测数据
logit_y_pred = logit_model.predict(logit_X_test)
# 5. 评估模型
logit_acc = logit_model.score(logit_X_test,logit_y_pred)
print("accuracy:", logit_acc)
# 5. 可视化
logit_X_view=np.linspace(-7,7,277)
logit_X_view = logit_X_view[:,np.newaxis]
def model(x):
    return 1/(1+np.exp(-x))
loss=model(logit_X_view*logit_model.coef_+logit_model.intercept_).ravel()
plt.figure('Logistic Regression')
plt.title('Logistic Regression')
plt.scatter(logit_X_train.ravel(), logit_y_train, color='lavender',zorder=17)
plt.plot(logit_X_view, loss, color='pink',linewidth=3)

lr_model=linear_model.LinearRegression()
lr_model.fit(logit_X_train,logit_y_train)
plt.plot(logit_X_view, lr_model.predict(logit_X_view), color='blue', linewidth=3)
plt.legend(('Logistic Regression','Linear Regression'),loc='lower right',fontsize='small')

# print info accuracy: 1.0