#https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.03-Bisection-Method.html

import numpy as np

def bisection(f, a, b, tol):
    """
    The Intermediate Value Theorem says that if f(x) is a continuous function 
    between a and b, and sign(f(a))≠sign(f(b)), then there must be a c, 
    such that a<c<b and f(c)=0.
 
    approximates a root, R, of f bounded by a and b to within tolerance
    | f(m) | < tol with m the midpoint between a and b Recursive implementation
    INPUT:
        var     type        example
        f       function    lambda x: x**2 - 2
        a       float       0
        b       float       2
        tol     float       0.1

    OUPUT:
        var     type        example
        yi      float       1.4375
    """
    
    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    # get midpoint
    m = (a + b)/2
    
    if np.abs(f(m)) < tol:
        # stopping condition, report m as root
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return bisection(f, a, m, tol)