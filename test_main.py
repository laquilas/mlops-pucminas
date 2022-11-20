from main import feature
import numpy as np

def test_answer_3():
    value_int,value_bis, value_intd1, value_qua, value_eig = feature(3)
    
    assert np.round_(value_int,5) == 0
    assert np.round_(value_bis,5) == 0
    assert np.round_(value_intd1,5) == 0


def test_answer_4():
    value_int,value_bis, value_intd1, value_qua, value_eig = feature(4)
    
    assert np.round_(value_int,5) == 0
    assert np.round_(value_bis,5) == 0
    assert np.round_(value_intd1,5) == 0

def test_answer_5():
    value_int,value_bis, value_intd1, value_qua, value_eig = feature(4)
    
    assert np.round_(value_int,5) == 0
    assert np.round_(value_bis,5) == 0
    assert np.round_(value_intd1,5) == 0    

def test_answer_5_a():
    value_int,value_bis, value_intd1, value_qua, value_eig = feature(4,[-3,2])
    
    assert np.round_(value_int,5) == -1.70557
    assert np.round_(value_bis,5) == 0.00049
    assert np.round_(value_intd1,5) == -2.09785  

def test_answer_5_a():
    value_int,value_bis, value_intd1, value_qua, value_eig = feature(4,[-3,2])
    
    assert np.round_(value_int,5) == -1.70557
    assert np.round_(value_bis,5) == 0.00049
    assert np.round_(value_intd1,5) == -2.09785     