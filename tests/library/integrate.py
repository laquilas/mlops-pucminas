import unittest
#import unittest
from _return_path import return_path
return_path()

from library.integrate import trapz_x

def test_integrate(x, y_pred):
    assert trapz_x(x) == y_pred

def test_integrate_error(x, y_pred):
    assert trapz_x(x) != y_pred    

if __name__ == "__main__":
    print("===== Test Integrate =====")
    x, y_pred =[1,2,3], 4
    test_integrate(x, y_pred)
    print(f"PASS 1")

    x,dx, y_pred =[1,2,3], 2, 8
    test_integrate_error(x, y_pred)
    print(f"PASS 2")
    print("========== END ==========")    


#test2
#x =[1,2,3]
#dx = 2
#y_pred = 8