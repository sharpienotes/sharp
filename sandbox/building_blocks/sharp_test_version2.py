
# WHAT THIS CODE DOES / IS SUPPOSED TO DO:
'''
todo:
 1) do a convolution with the sphere of the original data
 2) subtract this from the original data set
 3) then deconvolute
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

    # creates a temporary proxy for the data that follows later
    temp_data_proxy = np.random.random([3, 3, 3, 5, 4])
    # -------------------------------------------------------------------------#
    # COMPUTE THE CENTER POINT OF THE DATA, GIVEN AS A VECTOR (d COMPONENTS):
    center_mass = scipy.ndimage.measurements.center_of_mass(temp_data_proxy)
    #print('\n The center of the data is located at: '+ str(center_mass)+ '\n')

    # -------------------------------------------------------------------------#
    # READ IN THE SPHERE FUNCTION
    # IMPORTS:
    import itertools
    import numpy as np
    import scipy.ndimage

    # todo: make this a function

    data_temp_proxy = np.random.random([3, 3, 3, 5, 4])
    input_data = data_temp_proxy
    input_shape = input_data.shape
    print('Input shape is: ' + str(input_shape))
    input_dimension = len(input_shape)
    print('\nDimension of input data: ' + str(input_dimension))

    #sphere_center = scipy.ndimage.measurements.center_of_mass(input_data)
    sphere_center = center_mass
    print('\nSphere center: \n' + str(sphere_center))

    # ------------------------------------------------------------------------------#
    # filling the empty space which has the same size as the given input

    range_list = []
    # big list is the combination of all ranges of each dimension in space
    big_list = []

    for counter in range(0, input_dimension):
        dimension_range = input_shape[counter]
        range_list.append(dimension_range)
        big_list.append(np.arange(dimension_range))

    # this is the space filled by the input in terms of points:
    space_map = []

    for element in itertools.product(*big_list):
        space_points = element
        space_map.append(space_points)
    print('The space map at hand consists of ' + str(
        len(space_map)) + ' points. \n')

    # same dimensions as the input but filled with sphere
    sphere_map = space_map

    # calculation of radius of each point in this new space:
    # the new space has the dimensions of the input but is not filled with data!

    # pick a specific point in space one at a time
    radial_component_list = np.empty([len(space_map), 2])
    total_radii_list_per_space_point = list()
    sphere_map = np.zeros([len(space_map)], dtype=bool)
    for entry in range(0, len(space_map)):
        space_point = space_map[entry]
        point_all_radial_comp = 0.0
        radii_list = list()
        # walk through all its dimensions, one by one
        for dim in range(0, input_dimension):
            radial_component = (((space_point[dim]) - sphere_center[dim])) ** 2
            radii_list.append(radial_component)
            radius_here = np.sqrt(sum(radii_list))

        total_radii_list_per_space_point.append(radius_here)
        # desired_radius = sphere_radius
        desired_radius = 2
        # sphere_map is the boolean filled sphere, True in and False outside
        if radius_here < desired_radius:
            sphere_map[entry] = True
        else:
            sphere_map[entry] = False

    true_sphere_map = sphere_map.reshape(input_shape)

    # -------------------------------------------------------------------------#
    # PERFORM THE CONVOLUTION (I.E. MULTIPLICATION) OF SPHERE AND DATA
    import scipy
    from scipy import signal

    convolution = scipy.signal.convolve(data_temp_proxy, true_sphere_map, mode='same')
    # -------------------------------------------------------------------------#
    # SUBTRACT THE CONVOLUTION FROM THE ORIGINAL DATA (NOT TRANSFORMED!)
    difference = temp_data_proxy - convolution
    print("here we are: "+str(difference.shape))

    # -------------------------------------------------------------------------#
    # PERFORM THE DECONVOLUTION
    # todo: here we are:
    # cf: https://en.wikipedia.org/wiki/Richardson–Lucy_deconvolution
    # deconvolve apparently does not work in more than one dimension!!
    deconvolution = scipy.signal.deconvolve(difference, true_sphere_map)

    # -------------------------------------------------------------------------#
    # OUTPUT OF SHARP-CORRECTED DATA IN APPROPRIATE FORM:


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------------#
# APPENDIX:

