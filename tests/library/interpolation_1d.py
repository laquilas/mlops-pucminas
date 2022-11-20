# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.02-Linear-Interpolation.html
#import unittest

from _return_path import return_path
return_path()

from library.interpolation_1d import interpolation_1d

def test_interpolation_1d():
    x, y = [0, 1, 2], [1, 3, 2]
    x_test, y_pred = 1.5, 2.5
    assert interpolation_1d(x,y,x_test) == y_pred
    print(f"PASS 1")

if __name__ == "__main__":
    print("===== Test Bissection =====")
    test_interpolation_1d()
    print("========== END ==========")    


