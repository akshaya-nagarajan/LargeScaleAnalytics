################# KMEANS BELOW ##############################

## Initialisation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#[[1,7], [1,5], [2,9], [2,6], [3,9], [3,8], [3,6], [3,3], [4,8], [4,5], [5,7], [5,4], [6,9], [7,9], [7,3], [7,2], [8,7], [8,1]]
df = pd.DataFrame({
    'x': [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8],
    'y': [7, 5, 9, 6, 9, 8, 6, 3, 8, 5, 7, 4, 9, 9, 3, 2, 7, 1]
})


np.random.seed(200)
k = 3
centroids = {
    i+1: [np.random.randint(0, 9), np.random.randint(0, 10)]
    for i in range(k)
}
    
fig = plt.figure(figsize=(10, 10))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.show()

