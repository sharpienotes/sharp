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

#------------------------------------------------------------------------------#
# not sure if following maxima stuff is needed or correct
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
print('\nThe sphere in your space has radius: \n'+str(sphere_radius)+'\n')
#------------------------------------------------------------------------------#

# filling the empty space which has the same size as the given input
# the sphere is centered where the input data is centered as well

# todo: space should not be a list
space = np.empty(input_shape)

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
print('The space map at hand consists of '+str(len(space_map)) +' points. \n')

# same dimensions as the input but filled with sphere
sphere_map = space_map

# calculation of radius of each point in this new space:
# the new space has the dimensions of the input but is not filled with data!

# pick a specific point in space one at a time
radial_component_list=np.empty([len(space_map),2])
total_radii_list_per_space_point = list()

for entry in range(0,len(space_map)):
    space_point = space_map[entry]
    point_all_radial_comp = 0.0
    radii_list = list()
    # walk through all its dimensions, one by one
    for dim in range(0, input_dimension):
        # todo: is this even correct?
        radial_component = (((space_point[dim])-sphere_center[dim]))**2
        radii_list.append(radial_component)
        radius_here = np.sqrt(sum(radii_list))

    total_radii_list_per_space_point.append(radius_here)
    # todo: for radius_here smaller than radius assign number to space
    if radius_here < 2:
        sphere_map[entry] == 0
    else:
        sphere_map[entry] == 1


print(sphere_map[103])

space_radius = max(total_radii_list_per_space_point)
print('The radius of the artificial space is: '+str(space_radius))



# todo: comparing with previously computed radius

#------------------------------------------------------------------------------#
    #TODO compute sum of squares of entries and then square root
    # TODO compare this with radius previously computed
    # TODO then assign one or zero to the space itself and done



# print('TEST TEST TEST: '+str(space_point[1]))






















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
