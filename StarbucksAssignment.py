
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,7], [1,5], [2,9], [2,6], [3,9], [3,8], [3,6], [3,3], [4,8], [4,5], [5,7], [5,4], [6,9], [7,9], [7,3], [7,2], [8,7], [8,1]])
labels = range(1, 19)
plt.figure(figsize=(10, 7)) 
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:,0],X[:,1], label='True Position')
for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(-3, 3), textcoords='offset points', ha='right', va='bottom')
plt.show()

from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='single')
cluster.fit_predict(X)
plt.figure(figsize=(10, 7)) 
plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')

from scipy.cluster.hierarchy import dendrogram, linkage
print ("\n single link cluster \n") 
linked = linkage(X, 'single')
labelList = range(1, 20)
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.show()

from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='complete')
cluster.fit_predict(X)
plt.figure(figsize=(10, 7)) 
plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')

print ("\n complete link cluster \n")
linked_complete = linkage(X, 'complete') 
labelList = range(1, 20)
plt.figure(figsize=(10, 7)) 
dendrogram(linked_complete, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.show()

from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='average')
cluster.fit_predict(X)
plt.figure(figsize=(10, 7)) 
plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')

print ("\n average link cluster \n")
linked_average = linkage(X, 'average') 
labelList = range(1, 20)
plt.figure(figsize=(10, 7)) 
dendrogram(linked_average, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.show()

