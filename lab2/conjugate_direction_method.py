import numpy
import numpy as np
from typing import Callable

from scipy.optimize import minimize_scalar


def minimize_with_conjugate_direction_method(
        func: Callable[[np.ndarray], float],
        x0: np.ndarray,
        eps: float = 1e-3
):

    n = len(x0)
    start_x = x0.copy()
    direction_vectors = numpy.eye(n)
    k = 0
    while True:
        curr_x = start_x.copy()
        decreases_of_func = np.zeros(n)
        for i in range(n):
            lambda_func = lambda l: func(curr_x + l*direction_vectors[i])
            l_min = minimize_scalar(lambda_func).x
            func_before_direction = func(curr_x)

            curr_x += l_min*direction_vectors[i]
            decreases_of_func[i] = func_before_direction - func(curr_x)

        minimize_direction = curr_x - start_x

        if np.linalg.norm(minimize_direction) < eps:
            return curr_x

        idx_of_max_decrease = np.argmax(decreases_of_func)

        direction_vectors[idx_of_max_decrease] = minimize_direction / np.linalg.norm(minimize_direction)

        start_x = curr_x.copy()




A = 10
a = 2
b = 3
c = 1
d = 1
r = -1

def function(x):
    x1, x2 = x[0], x[1]
    exponent = - (1 / (10 - r**2)) * (
        (x1 - a)**2 / c**2 -
        2 * r * (x1 - a) * (x2 - b) / (c * d) +
        (x2 - b)**2 / d**2
    )
    return A - np.exp(exponent)


x0 = np.array([0.0, 0.0])

step_vector = np.array([0.5, 0.5])

x_opt = minimize_with_conjugate_direction_method(
    func=function,
    x0=x0,
    eps=1e-2,
)

print(f"x_opt = {x_opt}")

print(f"f_opt = {function(x_opt)}")
