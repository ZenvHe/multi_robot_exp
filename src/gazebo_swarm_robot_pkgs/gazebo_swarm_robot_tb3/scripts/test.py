import numpy as np

a = np.array([[2, 4, 3, 1, 5],
     [1, 3, 4, 2, 5],
     [3, 5, 2, 1, 4],
     [4, 2, 1, 3, 5],
     [6, 3, 2, 4, 1]])

#print(np.max(a, axis=0)[0])
a = a + 1
print(a)