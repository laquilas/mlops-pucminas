#https://pythonnumericalmethods.berkeley.edu/notebooks/chapter15.04-Eigenvalues-and-Eigenvectors-in-Python.html
#import unittest
import numpy as np
from _return_path import return_path
return_path()

from library.eigenvalues_eigenvectors import eig_value_vector

def conv_data(v,w, dec=5):
    v = np.round_(np.reshape(v,-1), decimals = dec)
    w = np.round_(np.reshape(w,-1), decimals = dec)
    return v,w

def test_eig_value_vector_1():
    a = np.array([[0, 2],[2, 3]])
    v = np.array([-1., 4.])
    w =  np.array([[-0.89442719,-0.4472136 ], [ 0.4472136,  -0.89442719]])
    
    v_p,w_p = eig_value_vector(a)
    
    v,w = conv_data(v,w)
    v_p,w_p = conv_data(v_p,w_p)

    assert np.array_equal(v_p,v), "Error Value"
    assert np.array_equal(w_p,w), "Error Vector"
    print(f"PASS 1")

def test_eig_value_vector_2():
    a = np.array([[2, 2, 4], [1, 3, 5], [2, 3, 4]])
    v = np.array([ 8.80916362, 0.92620912, -0.73537273])
    w = np.array([[-0.52799324, -0.77557092, -0.36272811],
        [-0.604391, 0.62277013, -0.7103262 ],
        [-0.59660259, -0.10318482,  0.60321224]])
    
    v_p,w_p = eig_value_vector(a)
    
    v,w = conv_data(v,w)
    v_p,w_p = conv_data(v_p,w_p)

    assert np.array_equal(v_p,v), "Error Value"
    assert np.array_equal(w_p,w), "Error Vector"
    print(f"PASS 2")


if __name__ == "__main__":
    print("===== Test eig_value_vector =====")
    test_eig_value_vector_1()
    test_eig_value_vector_2()
    print("========== END ==========")    

