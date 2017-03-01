
# WHAT THIS CODE DOES / IS SUPPOSED TO DO:
'''
todo:
-  fourier transorm of array of same size as data but filled with constant value
- get center of mass of this
- convolute with that
'''
# -----------------------------------------------------------------------------#
# IMPORTS: (necessary to execute the functions that are defined below)
import numpy as np
import scipy.ndimage
# -----------------------------------------------------------------------------#

import matplotlib.pyplot as plt


#from __future__ import (sphere_calculator) (not correct syntax yet)

# -----------------------------------------------------------------------------#
# DEFINITIONS: (of functions that can be used to compute the stuff)

# -----------------------------------------------------------------------------#
# ------------DEFINITION OF THE FUNCTION "sphere_calculator"-------------------#
# -----------------------------------------------------------------------------#

# DEFINITION OF THE FUNCTION:
def sphere_calculator(
        center=(0, 0, 0),
        radius=None,
        dimensions=None):
    """
    calculates the definition of a sphere based on input

    Args:
        center (tuple[int]):
            more text
        radius ():
        dimensions ():

    Returns:

    Examples:
        >>>

    """
    # if want to leave blank put None

    # -------------------------------------------------------------------------#
    #if center == None:
     #   center =

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

    Result = [center, radius, dimensions]
    return Result

# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# FUNCTION SPECIFIC IMPORTS:
import scipy
from scipy import signal

# FUNCTION THAT CONVOLUTES WITH THE SPHERE AS CALCULATED BY SPHERE_CALCULATOR
def sphere_convolutor(sphere_here,test):

    temp = sphere_calculator() # center, radius, dimensions
    if not sphere_here:
        sphere_here = np.empty([3,3,3], dtype = complex)

    for x in range(sphere_here.shape[0]):
        for y in range(sphere_here.shape[1]):
            for z in range(sphere_here.shape[2]):
                if np.sqrt(x*x + y*y + z*z)<=temp[1]:
                    sphere_here[x,y,z] = 1
                else:
                    sphere_here[x,y,z] = 0


    print('Here we are: '+str(sphere_here.dtype))
    plt.imshow(sphere_here[:, :, 1].astype(float))
    plt.colorbar()
    plt.show()
    quit()


    print(sphere_here)
    # test is to be substituted by the fourier transformed data
    if test == None:
        test = np.arange(27).reshape(3, 3, 3)

    convolution = scipy.signal.convolve(sphere_here, test)
    print('\n \n The convolution of sphere and test data is: \n'+ str(convolution))
    return


# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#

# the main function where all the interesting stuff happens:
def main():
    # GET THE INPUT DATA:(needs to be input the real stuff later, proxy for now)

    # creates a temporary proxy for the data that follows later, currently a
    # 3 dimensional matrix with 27 points filled in int steps from zero to 26
    temp_data_proxy = np.arange(27).reshape(3, 3, 3)
    #print(temp_data_proxy)
    #print(temp_data_proxy[1,1,1])


    # -------------------------------------------------------------------------#
    # COMPUTE THE CENTER POINT OF THE DATA, GIVEN AS A VECTOR (3 COMPONENTS):
    center_mass = scipy.ndimage.measurements.center_of_mass(temp_data_proxy)
    #print('\n The center of the data is located at: '+ str(center_mass)+ '\n')

    # -------------------------------------------------------------------------#
    # FAST FOURIER TRANSFORM OF THE DATA:
    fourier = np.fft.fftn(temp_data_proxy)
    #print(fourier.shape)
    print('\n The Fast Fourier Transform result is: \n'+ str(fourier)+'\n')

    # -------------------------------------------------------------------------#
    # READ IN THE SPHERE FUNCTION
    # choose an arbitrary radius for now here, TO BE CHANGED LATER!!!!!!!!!!

    abs_fourier = abs(fourier)
    # calculation of the center of the Fourier data:
    fourier_center = scipy.ndimage.measurements.center_of_mass(abs_fourier)
    #print(FourierCenter)

    fourier_range = abs_fourier.max()
    print('Here we are: '+str(fourier_range))

    # taking fourier_range ensures that all points of the space are inside!!
    # ball is the entire function of sphere calculation
    ball = sphere_calculator(fourier_center,50,None)


    # the sphere is defined as the first value (radius) of ball's output
    sphere = ball[1]
    # now the values as computed can be used in the following

    # VALUES AS COMPUTED BY THE SPHERE CALCULATOR:
    #print('The radius is: '+str(sphere))  (USEFUL)
    #print('The dimensions are: '+str(ball[2]))  (USEFUL)
    #print('The center is at: '+str(ball[0]))  (USEFUL)


    # -------------------------------------------------------------------------#
    # PERFORM THE CONVOLUTION (I.E. MULTIPLICATION) OF SPHERE AND DATA

    # convolution function is performed with original data since it is not yet
    # a multiplication in fourier space yet
    # sphere_convolutor uses the sphere to convolute
    convolution = sphere_convolutor(None, temp_data_proxy)

    # walking through the entire fourier transformed data and then check
    # each individual point for its length to see if it is in the sphere
    # then 'multiply' by sphere (zero or one out or in ,resp) for convolution

    #new_fourier = temp_data_proxy
    new_fourier = np.empty([3,3,3], dtype = complex)
    for x in range(fourier.shape[0]):
        for y in range(fourier.shape[1]):
            for z in range(fourier.shape[2]):
                point = fourier[x,y,z]
                # abs computes absolute value (vector length) of complex point
                length = abs(point)

                # values inside the sphere are assigned to new array
                if length <= sphere:
                    new_fourier[x,y,z] = fourier[x,y,z]

                # the ones outside the sphere are to be set to zero
                if length > sphere:
                    new_fourier[x,y,z] = fourier[x,y,z]*0

    #print('\n The abs of fourier before is: ')
    #print(abs(fourier))

    print('\n Convolution by own calculation yields: \n' +str(new_fourier))

    #--------------------------------------------------------------------------#


    # -------------------------------------------------------------------------#
    # SUBTRACT THE CONVOLUTION FROM THE ORIGINAL DATA (NOT TRANSFORMED!)
    # based on the self-written procedure for convolution with sphere
    subtraction = fourier - new_fourier
    print('\n \n Original data minus convoluted is: \n' + str(subtraction))

    # -------------------------------------------------------------------------#
    # PERFORM THE DECONVOLUTION


    # -------------------------------------------------------------------------#
    # OUTPUT OF SHARP-CORRECTED DATA IN APPROPRIATE FORM:


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------------#
# APPENDIX:

