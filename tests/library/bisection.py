#import unittest
from _return_path import return_path
return_path()

from library.bisection import bisection

def test_bisection(f,x, y, tol, y_pred):
    assert bisection(f,x,y,tol) == y_pred

if __name__ == "__main__":
    print("===== Test Bissection =====")
    f = lambda x: x**2 - 2
    x, y, tol, y_pred = 0, 2, 0.1, 1.4375
    test_bisection(f,x, y, tol, y_pred)
    print(f"PASS 1")
    
    f = lambda x: x**2 - 2
    x, y, tol, y_pred = 0, 2, 0.01, 1.4140625
    test_bisection(f,x, y, tol, y_pred)
    print(f"PASS 2")
    print("========== END ==========")    
