import numpy as np

X = np.array(range(100))
X = X.reshape((10,10))
print(X)

print("Selected rows:") 
Y = np.random.choice(range(len(X)), 3, replace=False) 
print(X[Y])

