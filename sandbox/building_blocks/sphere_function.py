# IMPORTS:
import itertools
import numpy as np
import scipy.ndimage

data_temp_proxy = np.random.random([3,3,3,5,4])
input_data = data_temp_proxy
input_shape = input_data.shape
print('Input shape is: '+str(input_shape))
input_dimension = len(input_shape)
print('\nDimension of input data: '+str(input_dimension))

sphere_center = scipy.ndimage.measurements.center_of_mass(input_data)
print('\nSphere center: \n'+str(sphere_center))


multi_max = []
maxima_list = []

for axis in range(0,input_dimension):
    multi_max_entries = np.amax(input_data, axis=axis)
    multi_max.append(multi_max_entries)
    maxima_list_entries = np.amax(multi_max_entries)
    maxima_list.append(maxima_list_entries)
print('\nMaxima: \n'+str(maxima_list) +'\n')


radial_components = []
for runner in range(0,input_dimension):
    radial_components.append((maxima_list[runner]-sphere_center[runner])**2)

component_sum = sum(radial_components)
sphere_radius = np.sqrt(component_sum)
print(sphere_radius)


space = np.empty(input_shape)
for index in range(itertools.product()):
    print('hello')
    #sphere = 1 if point components smaller radius
    # sphere = 0 if bigger















# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# DEFINITION OF THE FUNCTION:
def sphere_calculator(center = (1,1,1), radius = 1, dimensions = (1,1,1)):
    # TODO: input the right description
    # -------------------------------------------------------------------------#
    # TODO: n dimensional case of input with itertools.product
    if dimensions:
        radius = dimensions[0]

    if radius:
        dimensions = (radius, radius, radius)

    x0 = center[0]
    y0 = center[1]
    z0 = center[2]

    # -------------------------------------------------------------------------#

    # SPAN OF SPHERE (i.e. maximal values in each direction, half-axis length):
    x_span = dimensions[0]
    y_span = dimensions[1]
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
    sphere_parameters = [center, radius, dimensions]

    # creation of a sphere in space
    # TODO: space flexible to the n dimensional input dimensions and shapes!
    space2 = np.empty([3,3,3])




    return sphere_parameters


# -----------------------------------------------------------------------------#
# -----------------------------------------------------------------------------#
# CALLING THE FUNCTION:
#sphere_calculator((-4, -3, 0), 2, None)
#sphere_calculator((1,1,1), None, None)
sphere_calculator()
# sphere_calculator((None, None, None))
# sphere_calculator((None, 1, None))


# sphere = point <= radius       # is the condition to be inside or on a sphere
