import itertools
import numpy as np

i = [1, 1, 1]
j = [0, 1, 2]
c = [i,j]

# equivalent to nested for loops:
for element in itertools.product([i],[j],repeat=2):
    new_list = element
    print(new_list)
    print(new_list[1])
    aaa = new_list[1]
    print(aaa[1])

# arrays and stuff:
sphere_here = np.empty([3,3,3], dtype = complex)
# note: random is between zero and one
data_temp_proxy = np.random.random([3,3,3,5,4])
a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim, a.shape)
print(a.itemsize)
print(a.size)

# b is called a tuple
b = (1,2,3,4)
print(len(b))



