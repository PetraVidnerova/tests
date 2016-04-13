from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt 

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)

x = np.array([0, 0])
distances, indices = nbrs.kneighbors(x)

print(distances)
print(indices) 

neighbors = X[indices[0]]
print(neighbors)

plt.plot(X[:,0], X[:,1], 'ro') 
plt.plot(x[0], x[1], 'bo')
plt.plot(neighbors[:,0], neighbors[:,1], 'go')
plt.show() 
