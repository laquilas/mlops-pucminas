import unittest
#import unittest
from _return_path import return_path
return_path()

from library.integrate import trapz_x

def test_integrate_1():
    x, y_pred =[1,2,3], 4
    assert trapz_x(x) == y_pred
    print(f"PASS 1")

def test_integrate_2():
    x,dx, y_pred =[1,2,3], 2, 8
    assert trapz_x(x) != y_pred 
    print(f"PASS 2")   

if __name__ == "__main__":
    print("===== Test Integrate =====")
    test_integrate_1()
    test_integrate_2()
    print("========== END ==========")    
