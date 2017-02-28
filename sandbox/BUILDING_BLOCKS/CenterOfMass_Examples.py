# tools useful if one wants to compute the center of mass of an array at hand

import numpy as np
import scipy.ndimage


# -----------------------------------------------------------------------------#
# creates 3 dimensional array
c = np.arange(27).reshape(3, 3, 3)

# -----------------------------------------------------------------------------#
# print() gives output on screen with the text and the vector, str() just
# makes sure it can be  output correctly in one command with text, strictly
# could separate the two but not necessary here
print('This array was used as input:  \n' + str(c))

# -----------------------------------------------------------------------------#
from scipy import ndimage as sim

# is the package that is used to compute the center (of mass), call it sim in
#  shorthand

# computes the center (of mass) of the array specified
cmc = scipy.ndimage.measurements.center_of_mass(c)

# outputs the center of mass
print('\n The center of the array lies at the following coordinates: '
      + str(cmc) + '\n')

# -----------------------------------------------------------------------------#

# creates a 3 dim array with any input of data type float64
e = np.empty((3, 3, 3), dtype=np.float64)

# fills the whole array with the value 1 of data typefloat64
e.fill(1)

print(e)
# computes the center of mass of the array e that was filled with nothing
cme = scipy.ndimage.measurements.center_of_mass(e)

# outputs the center of mass
print('\n The center of the new array lies at the following coordinates: '
      + str(cme))

# -----------------------------------------------------------------------------#
