import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_blobs

# K-means 任务为聚类 n_classes=5
from sklearn.cluster import KMeans

# 1. 准备数据
kmeans_X_data, kmeans_y_data = make_blobs(n_samples=500, centers=5, cluster_std=0.60, random_state=0)
# 2. 训练模型
kmeans_model = KMeans(n_clusters=5)
kmeans_model.fit(kmeans_X_data)
# 3. 预测模型
kmeans_y_pred = kmeans_model.predict(kmeans_X_data)
# 4. 可视化
plt.figure('K-Means')
plt.title('K-Means')
plt.scatter(kmeans_X_data[:,0], kmeans_X_data[:, 1], s=50)
plt.scatter(kmeans_X_data[:, 0], kmeans_X_data[:, 1], c=kmeans_y_pred, s=50, cmap='viridis')
centers = kmeans_model.cluster_centers_
plt.scatter(centers[:,0], centers[:, 1], c='red', s=80, marker='x')
plt.show()