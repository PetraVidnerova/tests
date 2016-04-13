import numpy as np 
import matplotlib.pyplot as plt 

k = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
ver1 = np.random.random(len(k)) 
ver2 = np.random.random(len(k))

    
line1, = plt.plot(k, ver1, "ro--", label="ver1") 
line2, = plt.plot(k, ver2, "bo--", label="ver2")
plt.legend(handles=[line1, line2]) 
plt.xlabel("number of hidden units") 
plt.ylabel("mean error")
plt.show() 
