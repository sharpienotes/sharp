import scipy

# IMPORTS:
import numpy as np
from scipy import signal
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# DEFINITION OF THE FUNCTION:
def sphere_calculator(center = None, radius = None, dimensions = None):
    "calculates the definition of a sphere based on input"

    # -------------------------------------------------------------------------#
    if center == None:
        center = (0, 0, 0)

    if radius == None:
        radius = 1
        if dimensions:
            radius = dimensions[0]

    if dimensions == None:
        if radius == None:
            dimensions = (1, 1, 1)
        if radius:
            dimensions = (radius, radius, radius)

    # CENTERING:
    # the x component of the center of the sphere
    x0 = center[0]
    # the y component of the center of the sphere
    y0 = center[1]
    # the z component of the center of the sphere
    z0 = center[2]

    # -------------------------------------------------------------------------#

    # SPAN OF SPHERE (i.e. maximal values in each direction, half-axis length):
    # is the span of the sphere's x-axis component
    x_span = dimensions[0]
    # is the span of the sphere's y-axis component
    y_span = dimensions[1]
    # is the span of the sphere's z-axis component
    z_span = dimensions[2]

    # -------------------------------------------------------------------------#

    # computation of the radius of the sphere
    if not radius:
        radius = np.sqrt(
            (x_span - x0) ** 2 + (y_span - y0) ** 2 + (z_span - z0) ** 2)

    # -------------------------------------------------------------------------#

    # FINAL OUTPUT OF THE FUNCTION:

    # output if you put in something that does not actually exist
    if radius != (1 / 3) * (dimensions[0] + dimensions[1] + dimensions[2]):
        print(
            'You may want to check your input, this radius and dimension are '
            'incompatible!')

    # output if everything seems to have worked fine:
    else:
        print(
            'Congratulations, your sphere is centered at ' + str((x0, y0, z0))
            + ', has radius ' + str(radius) + ' and a span of '
            + str(dimensions)
            + ' in each corresponding direction from the center.')


    list2 = [center, radius, dimensions]
    return list2


# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# FUNCTION THAT CONVOLUTES WITH THE SPHERE AS CALCULATED BY SPHERE_CALCULATOR
def sphere_convolutor(sphere_here,test):
    'is the convolution with the sphere definied with sphere_calculator'
    temp = sphere_calculator(None, None, None) # center, radius, dimensions
    if not sphere_here:
        sphere_here = np.empty([3,3,3], dtype = complex)

    for x in range(sphere_here.shape[0]):
        for y in range(sphere_here.shape[1]):
            for z in range(sphere_here.shape[2]):
                if np.sqrt(x*x + y*y + z*z)<=temp[1]:
                    sphere_here[x,y,z] = 1
                else:
                    sphere_here[x,y,z] = 0

    print(sphere_here)
    # test is to be substituted by the fourier transformed data
    if test == None:
        test = np.arange(27).reshape(3, 3, 3)

    convolution = scipy.signal.convolve(sphere_here, test)
    print('\n \n The convolution of sphere and test data is: \n'+ str(convolution))
    return convolution




# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# FUNCTION THAT CONVOLUTES THE ORIGINAL DATA WITH SHERE BY MEANS OF FFT
def other_sphere_convolutor(sphere_here, test):
    #'FUNCTION THAT CONVOLUTES THE ORIGINAL DATA WITH SHERE BY MEANS OF FFT'
    temp = sphere_calculator(None, None, None) # center, radius, dimensions
    if not sphere_here:
        sphere_here = np.empty([3,3,3], dtype = complex)

    for x in range(sphere_here.shape[0]):
        for y in range(sphere_here.shape[1]):
            for z in range(sphere_here.shape[2]):
                if np.sqrt(x*x + y*y + z*z)<=temp[1]:
                    sphere_here[x,y,z] = 1
                else:
                    sphere_here[x,y,z] = 0

    if test == None:
        test = np.arange(27).reshape(3, 3, 3)
    other_convolution = scipy.signal.fftconvolve(sphere_here, test)
    print('\n The result of other convolution with sphere by fft is: \n '
          ''+str(other_convolution))
    return other_convolution

# running the actual function:
other = other_sphere_convolutor(None, None)
first_convolution = sphere_convolutor(None, None)
comparison = other - first_convolution
print('\n \n The comparison yields a difference of: \n '+str(comparison))
print('\n The output dimensions are: \n'+str(comparison.shape))
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#

# DATA PLOT TRIAL FOR COMPARISON VISUALIZATION:


import pylab
import numpy

import matplotlib.pyplot as plt


#x1 = np.linspace(0, 10, 20)
#y1 = np.sin(x1)

#2 = np.linspace(0, 10, 1000)
#y2 = np.sin(x2)


#pylab.plot(x1, y1, 'bo', label='sampled')
#pylab.plot(x2, y2, ':k', label='continuous')
#pylab.legend()

#pylab.ylim(-1.5, 2.0)
#pylab.show()

#pylab.hist(comparison) (does not work with 3d array of 5,5,5 dimension)
x1 = np.linspace(-100,100,1)
x2 = comparison[0,:,:]
print('\n All values summed up: '+str(numpy.sum(comparison))+'\n')
mean_comparison = numpy.sum(comparison)/(5*5*5)
# to see if the two methods yield the same results, the sum of the differences
# is divided by the number of total elements
print('The total mean comparison is: '+str(mean_comparison)+'\n')
print(x2)
print(x2.shape)
y1 = np.linspace(-100,100,1)
#pylab.plot(x1,y1)
pylab.show()



import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import nibabel as nb
import numpy as np

comparison = comparison.astype(np.float64)
sns.pointplot(comparison[0,:,:])
print(comparison[0,:,:])
sns.plt.show()
















# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# DECONVOLUTION:
