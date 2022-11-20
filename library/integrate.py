# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapezoid.html#scipy.integrate.trapezoid

import numpy as np

def trapz_x(x):
    """
    Integrate along the given axis using the composite trapezoidal rule.

    INPUT:
        var     type        example
        x       array       [1, 2, 3]

    OUPUT:
        var     type        example
        yi      float       4
    """    
    return np.trapz(x)