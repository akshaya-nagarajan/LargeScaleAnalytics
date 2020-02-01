
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt

X = np.array([[3,7], [2,6], [2,2], [5,8], [5,5], [5,2], [6,6], [8,4], [7,3], [10,6], [12,8]])
labels = range(1, 12)
plt.figure(figsize=(10, 7)) 
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:,0],X[:,1], label='True Position')
for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(-3, 3), textcoords='offset points', ha='right', va='bottom')
plt.show()

from scipy.cluster.hierarchy import dendrogram, linkage
print ("\n single link cluster \n") 
linked = linkage(X, 'single')
labelList = range(1, 13)
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.show()

print ("\n complete link cluster \n")
linked_complete = linkage(X, 'complete') 
labelList = range(1, 13)
plt.figure(figsize=(10, 7)) 
dendrogram(linked_complete, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.show()

print ("\n average link cluster \n")
linked_average = linkage(X, 'average') 
labelList = range(1, 13)
plt.figure(figsize=(10, 7)) 
dendrogram(linked_average, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.show()

