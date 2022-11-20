# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.quadratic_assignment.html#scipy.optimize.quadratic_assignment
#import unittest
import numpy as np

from _return_path import return_path
return_path()
from library.optimize import opt_quadratic_assignment

def test_quadratic_assignment(A,B,y_pred, dec=5):
    result = opt_quadratic_assignment(A,B)
    col_ind = np.round_(np.reshape(np.array(result.col_ind),-1), decimals = dec)
    y_col_ind = np.round_(np.reshape(y_pred['col_ind'],-1), decimals = dec)
    assert  result.fun == y_pred['fun']
    assert  result.nit == y_pred['nit']
    assert  np.array_equal(col_ind,y_col_ind), "Error Value"


if __name__ == "__main__":
    print("===== Test optimize =====")
    A = np.array([[0, 80, 150, 170], [80, 0, 130, 100], [150, 130, 0, 120], [170, 100, 120, 0]])
    B = np.array([[0, 5, 2, 7], [0, 0, 3, 8], [0, 0, 0, 3], [0, 0, 0, 0]])
    y_pred = { "col_ind": np.array([0, 3, 2, 1]), "fun": 3260, "nit": 9}

    test_quadratic_assignment(A,B,y_pred)
    print(f"PASS 1")
    print("========== END ==========")  
