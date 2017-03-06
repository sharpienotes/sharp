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

print('######################################')
# arrays and stuff:
sphere_here = np.empty([3,3,3], dtype = complex)
# note: random is between zero and one
data_temp_proxy = np.random.random([3,3,3,5,4])
a = np.arange(15).reshape(3, 5)
print(a)
print('######################################')
print(a.ndim, a.shape)
print(a.itemsize)
print(a.size)

# b is called a tuple
b = (1,2,3,4)
print('how to get the length of a tuple: '+str(len(b)))
print('how to call an element in a tuple: '+str(b[1]))
print('######################################')
sl = slice(*a)
print(sl)

# getting a list of two lists a and b:
complete_sphere = list(zip(a,b))

# getting a list of all values "True":
truelist = [entry for entry in complete_sphere if entry[1] == True]


# common errors:
# off by one in indexing
# single = where one would need ==

# defining a function:
# if want to be able to call empty, function() then specifying as follows is a good idea:
def function(a=None, b=None, point=None):
    """

    Args:
        a ():
        b ():

    Returns: the sum of a and b

    """
    if not a:
        a=5
    if not b:
        b=6

    # if want to leave this empty but the parameter is an array:
    # use:
    if point is None:
        point = (1,2,3)

    other_point = point + a
    print(other_point)

    return a+b

function() # calls the function without specified non-default parameters


