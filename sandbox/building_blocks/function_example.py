
def summing(
        a,
        b):
    """

    Args:
        a ():
        b ():

    Returns:

    Examples:
        >>> summing(7, 10)
        17
    """
    return a + b

# defining a function:
# if want to be able to call empty, function() then specifying as follows is a good idea:
def function(a=None, b=None, point=None):
    """

    Args:
        a ():
        b ():

    Returns: the sum of a and b

    """
    if not a:
        a=5
    if not b:
        b=6

    # if want to leave this empty but the parameter is an array:
    # use:
    if point is None:
        point = (1,2,3)

    other_point = point + a
    print(other_point)

    return a+b

function() # calls the function without specified non-default parameters
