# IMPORTS:
import numpy as np
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
# CALLING THE FUNCTION:
#sphere_calculator((-4, -3, 0), 2, None)
#sphere_calculator((1,1,1), None, None)
sphere_calculator((-4, -3, 0), 2, None)
# sphere_calculator((None, None, None))
# sphere_calculator((None, 1, None))


# sphere = point <= radius       # is the condition to be inside or on a sphere
