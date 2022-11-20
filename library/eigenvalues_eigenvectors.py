# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter15.04-Eigenvalues-and-Eigenvectors-in-Python.html

import numpy as np
from numpy.linalg import eig

def eig_value_vector(a):

    """
    In order to get the eigenvalues and eigenvectors, from Ax=λx, we can get the following form:    (A-λI)x=0
    Where I is the identify matrix with the same dimensions as A. If matrix A-λI has an inverse, 
    then multiply both sides with (A-λI)^-1, we get a trivial solution x=0. Therefore, 
    when A-λI is singular (no inverse exist), we have a nontrivial solution, which means that the determinant is zero:
    det(A-λI)=0
    this equation is called characteristic equation, which will lead to a polynomial equation for λ, 
    then we can solve for the eigenvalues.

    INPUT:
        var     type        example
        a       array       [[0, 2], [2, 3]]

    OUPUT:
        var     type        example
        v       float       4
        w       array
    """
    w,v=eig(a)
    return np.array(w),np.array(v)