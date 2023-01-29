import numpy as np

a= [[[11,22,33],[4,2,2],[1,1,1]],[[1,1,1],[11,12,33],[4,3,2]]]

b = np.array(a)
print(b.ndim)
print(b.shape)
b[1][0] = b[1][1]+b[0][0]
print(b[0])

print(np.dot(b[0],b[1]))

#tensor

