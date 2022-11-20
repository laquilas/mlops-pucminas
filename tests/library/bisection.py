#import unittest
import pytest
from _return_path import return_path
return_path()

from library.bisection import bisection

def test_bisection_1():
    f = lambda x: x**2 - 2
    x, y, tol, y_pred = 0, 2, 0.1, 1.4375
    assert bisection(f,x,y,tol) == y_pred
    print(f"PASS 1")

def test_bisection_2():
    f = lambda x: x**2 - 2
    x, y, tol, y_pred = 0, 2, 0.01, 1.4140625
    assert bisection(f,x,y,tol) == y_pred
    print(f"PASS 2")


if __name__ == "__main__":
    print("===== Test Bissection =====")
    test_bisection_1()
    test_bisection_2()
    print("========== END ==========")    
