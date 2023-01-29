#https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/XCjRw/one-dimensional-numpy
#%%
import numpy as np
import matplotlib.pyplot as plt

### Basic
# numpy array can only store one type of elements
a = np.array([0,3,2,99])
b = np.array([0,1,2,1])
c = np.array([0,1,1,3])

# numpy array is basiccaly a vector /matrix

print(a.dtype) #get the type of elements that the array stored
print(a.size) #get the number of elements in the array
print(a.ndim) # get the dimansion of the array
print(a.shape) # get the number of dimension and size of each dimension

### Indexing and Slicing
print(a[3])
a[3] = "8"+"0" #when change to number string, the element automaticcaly stored as int or float
print(a[3])

### Operations
# Basic
print(a+b)
print(b-1)
print(c<b)
print(b*c)
print(np.dot(a,b)) #calculate dot product

print(a.mean())
print(a.max())
# Universal
print(np.e) # the euler number
print(np.pi) # the number pi

print(np.sin(a)) #return a new element, not affect the variable
print(a)
# creat an array that contains evenly distributed numbers
# with the given starting and ending number and 
# the amount of number that has to be generated
x = np.linspace(-2,3*np.pi,num=100)
y = np.sin(x)
plt.plot(x,y)