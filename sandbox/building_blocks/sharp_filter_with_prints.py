import numpy as np

def sharp_filter(
        input_data = None,
        sphere_center= None,
        desired_sphere_radius= None):
    """

    Args:
        input_data ():     data that is to be filtered using SHARP
        sphere_center ():  center of sphere used for performing the filtering,
                           by default the center of the input data
        desired_sphere_radius (): the radius of the sphere that is used for filtering

    Returns:
                           input data after filter is applied in same shape

    """

    import numpy as np
    import itertools
    import scipy.ndimage

    if input_data is None:
        data_temp_proxy = np.random.random([3, 3, 3, 5, 4])
        input_data = data_temp_proxy

    center_mass = scipy.ndimage.measurements.center_of_mass(input_data)
    input_shape = input_data.shape
    print('Input shape is: ' + str(input_shape))
    input_dimension = len(input_shape)
    print('\nDimension of input data: ' + str(input_dimension))

    if sphere_center == None:
        sphere_center = center_mass
    print('\nSphere center: \n' + str(sphere_center))


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

    if desired_sphere_radius == None:
            desired_sphere_radius = 2
    # pick a specific point in space one at a time
    total_radii_list_per_space_point = list()
    sphere_map = np.zeros([len(space_map)], dtype=bool)
    for entry in range(0, len(space_map)):
        space_point = space_map[entry]
        radii_list = list()

        # walk through all its dimensions, one by one
        for dim in range(0, input_dimension):
            radial_component = (((space_point[dim]) - sphere_center[dim])) ** 2
            radii_list.append(radial_component)
            radius_here = np.sqrt(sum(radii_list))

        total_radii_list_per_space_point.append(radius_here)

        # sphere_map is boolean filled space, True in and False outside sphere
        if radius_here < desired_sphere_radius:
            sphere_map[entry] = True
        else:
            sphere_map[entry] = False

    true_sphere_map = sphere_map.reshape(input_shape)

    # PERFORM THE FFT OF SPHERE AND DATA AND MULTIPLY THE TWO (~ convolution)
    import scipy
    from scipy import fftpack

    data_fft = scipy.fftpack.fftn(input_data)
    sphere_fft = scipy.fftpack.fftn(true_sphere_map)
    convolution = data_fft * sphere_fft

    # SUBTRACT THE 'CONVOLUTION' FROM THE ORIGINAL RAW DATA
    difference = input_data - convolution

    # PERFORM INVERSE FOURIER TRANSOFRM
    modified_data_back_fft = scipy.fftpack.ifftn(difference)
    filtered_data = modified_data_back_fft
    return filtered_data

sharp_filter(np.random.random([3, 3, 3, 5, 4]), (0,0,0,0,0), 1)
#sharp_filter()
