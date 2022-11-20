import sys
def return_path(path_test = "tests"):
    path = sys.path[0]
    for return_folder, folder in enumerate(path.split("\\")):
        if folder == path_test: break
    return_folder = return_folder - len(path.split("\\"))
    # Return folder(s)
    new_path = "\\".join(sys.path[0].split("\\")[:return_folder])
    sys.path.append(new_path)
return_path()

from library.integrate import trapz_x
from library.bisection import bisection
from library.eigenvalues_eigenvectors import eig_value_vector
from library.interpolation_1d import interpolation_1d
from library.optimize import opt_quadratic_assignment


import numpy as np



def feature(N = 6,inter = [-1.5,1.5],tol = 0.001):
    x1 = np.linspace(*inter,N**2)
    y1 = np.sin(x1)
    yt = 1.23 * x1
    A = np.reshape(x1,(N,-1))
    B = np.reshape(y1,(N,-1))
    value_int = trapz_x(y1)
    value_bis = bisection(np.sin,*inter,tol)
    value_intd1 = interpolation_1d(x1,yt,value_int)
    value_qua = opt_quadratic_assignment(A,B)
    value_eig = eig_value_vector(A)
    return value_int,value_bis, value_intd1, value_qua, value_eig

if __name__ == "__main__":
    print(feature(5,[-3,2]))
    