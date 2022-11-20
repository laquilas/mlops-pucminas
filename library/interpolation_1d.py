# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.02-Linear-Interpolation.html
from scipy.interpolate import interp1d

def interpolation_1d(x,y,xi):
    """
    In linear interpolation, the estimated point is assumed to lie on the line joining 
    the nearest points to the left and right. 

    INPUT:
        var     type        example
        x       array       [0, 1, 2]
        y       array       [1, 3, 2]
        xi      float       1.5

    OUPUT:
        var     type        example
        yi      float       2.5
    """
    f = interp1d(x, y)
    y_hat = f(xi)
    return y_hat