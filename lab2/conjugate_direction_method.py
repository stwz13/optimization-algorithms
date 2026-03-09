import numpy as np
from typing import Callable

from fontTools.misc.cython import returns
from pygments.unistring import xid_start
from scipy.optimize import minimize_scalar

def minimize_with_conjugate_direction_method(
        func: Callable[[np.ndarray], float],
        x0: np.ndarray,
        eps: float = 1e-3
):
    k = 0
    n = len(x0)
    last_x = x0.copy()

    while True:
        s_k = np.zeros(n)
        s_k[0] = 1
        lamb_func = lambda l: func(last_x + l * s_k)
        l = minimize_scalar(lamb_func).x
        x_new = last_x + l * s_k
        last_x = x_new

        for i in range(1,n):
            e_k = np.zeros(n)
            e_k[i] = 1

            y_prev = last_x + e_k
            y_k = y_prev.copy()
            for j in range(i + 1):
                s_j = np.zeros(n)
                s_j[j] = 1
                lamb_func = lambda l: func(y_k + l * s_j)
                l = minimize_scalar(lamb_func).x
                y_k += l * s_j

            s_k = y_k - y_prev

            lamb_func = lambda l: func(last_x + l*s_k)
            l = minimize_scalar(lamb_func).x
            x_next = last_x + l*s_k
            curr_x = x_next

            if np.linalg.norm(curr_x - last_x) < eps:
                return curr_x

            k += 1


