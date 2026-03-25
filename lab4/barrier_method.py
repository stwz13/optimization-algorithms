from typing import Callable, List
import numpy as np
from scipy.optimize import minimize

def minimize_with_barrier_method(func: Callable[[np.ndarray], float],
                   g: List[Callable[[np.ndarray], float]],
                   x0: np.ndarray,
                   r : float = 1, eps: float = 0.1, coef: float = 0.2):

    x_curr = x0
    while r > eps:

        barrier_func = lambda x: func(x) - r * np.sum([np.log(gi(x)) for gi in g])

        x_curr = minimize(barrier_func, x_curr, method='Nelder-Mead').x

        r *= coef
    return x_curr

function = lambda x: x[0]**2 - 2*x[0] + x[1]**2 + x[1]

limitations = [lambda x: -x[0]**2 + x[1], lambda x: -x[1] + 5]

x0 = np.array([0, 1])

result = minimize_with_barrier_method(function, limitations, x0, eps=0.05)

print(result)