# IMPORTS:
import itertools
import numpy as np
import scipy.ndimage

# todo: make this a function
# todo: reduced space in spherical form from original data same size then convol.

data_temp_proxy = np.random.random([3,3,3,5,4])
input_data = data_temp_proxy
input_shape = input_data.shape
print('Input shape is: '+str(input_shape))
input_dimension = len(input_shape)
print('\nDimension of input data: '+str(input_dimension))

sphere_center = scipy.ndimage.measurements.center_of_mass(input_data)
print('\nSphere center: \n'+str(sphere_center))

#------------------------------------------------------------------------------#
# filling the empty space which has the same size as the given input
# the sphere is centered where the input data is centered as well

#space = np.empty(input_shape) not the correct definition

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
radial_component_list = np.empty([len(space_map),2])
total_radii_list_per_space_point = list()
local_counter = 0
other_counter = 0
# sphere_map gives the sphere as boolean values depending if the point they
# belong to is in our outside the radius specified
sphere_map = np.zeros([len(space_map)], dtype = bool)
for entry in range(0,len(space_map)):
    space_point = space_map[entry]
    point_all_radial_comp = 0.0
    radii_list = list()
    # walk through all its dimensions, one by one
    for dim in range(0, input_dimension):
        radial_component = (((space_point[dim])-sphere_center[dim]))**2
        radii_list.append(radial_component)
        radius_here = np.sqrt(sum(radii_list))

    total_radii_list_per_space_point.append(radius_here)
    #desired_radius = sphere_radius
    desired_radius = 2

    if radius_here < desired_radius:
        sphere_map[entry] = space_map[entry] #(was boolean True)
        local_counter += 1
    else:
        sphere_map[entry] = np.nan #(was boolean False)
        other_counter +=1

#print(sphere_map[14])
#complete_sphere = np.array(space_map,sphere_map)
complete_sphere = list(zip(space_map,sphere_map))
#print(len(sphere_map))
# some print stuff:
space_radius = max(total_radii_list_per_space_point)
print('The maximal radius of the artificial space is: '+str(space_radius))
print('All together are: '+str(local_counter))
#print(complete_sphere)
print(complete_sphere[539])
print(other_counter)
print(other_counter+local_counter)
truelist = [entry for entry in complete_sphere if entry[1] == True]
print(sphere_map)
#------------------------------------------------------------------------------#
