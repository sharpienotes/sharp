
# WHAT THIS CODE DOES / IS SUPPOSED TO DO:
'''
todo:
-  fourier transorm of array of same size as data but filled with constant value
- get center of mass of this
- convolute with that
'''
# -----------------------------------------------------------------------------#
# IMPORTS: (necessary to execute the functions that are defined below)
# -----------------------------------------------------------------------------#

import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------#
# DEFINITIONS: (of functions that can be used to compute the stuff)
# -----------------------------------------------------------------------------#

# the main function where all the interesting stuff happens:
def main():
    import numpy as np
    import scipy.ndimage

    # GET THE INPUT DATA:(needs to be input the real stuff later, proxy for now)

    # creates a temporary proxy for the data that follows later, currently a
    # 3 dimensional matrix with 27 points filled in int steps from zero to 26
    temp_data_proxy = np.random.random([3, 3, 3, 5, 4])

    # todo: get a sphere
    # todo: do a convolution with the sphere of the original data
    # todo: subtract this from the original data set
    # todo: then deconvolute
    # -------------------------------------------------------------------------#
    # COMPUTE THE CENTER POINT OF THE DATA, GIVEN AS A VECTOR (3 COMPONENTS):
    center_mass = scipy.ndimage.measurements.center_of_mass(temp_data_proxy)
    #print('\n The center of the data is located at: '+ str(center_mass)+ '\n')

    # -------------------------------------------------------------------------#
    # READ IN THE SPHERE FUNCTION

    # -------------------------------------------------------------------------#
    # PERFORM THE CONVOLUTION (I.E. MULTIPLICATION) OF SPHERE AND DATA
    import scipy
    from scipy import signal
    # the sphere is: complete_sphere
    # scipy.signal.convolve(in1, in2, mode='full') (use mode same)
    sphere = np.asarray(complete_sphere)
    convolution = scipy.signal.convolve(data_temp_proxy, sphere, mode='same')
    print(len(convolution))
    # make one and zero out of booleans
    # multiply that with the original space

    # reduced space in spherical form from original data same size then convol.
    # -------------------------------------------------------------------------#
    # SUBTRACT THE CONVOLUTION FROM THE ORIGINAL DATA (NOT TRANSFORMED!)

    # -------------------------------------------------------------------------#
    # PERFORM THE DECONVOLUTION


    # -------------------------------------------------------------------------#
    # OUTPUT OF SHARP-CORRECTED DATA IN APPROPRIATE FORM:


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------------#
# APPENDIX:

