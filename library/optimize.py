# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.quadratic_assignment.html#scipy.optimize.quadratic_assignment
from scipy.optimize import quadratic_assignment
import numpy as np

def opt_quadratic_assignment(A,B):

    res = quadratic_assignment(A, B)
    return res