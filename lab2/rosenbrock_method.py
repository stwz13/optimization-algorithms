from typing import Callable
import numpy as np
from scipy.optimize import minimize_scalar


def minimize_with_rosenbrok_method(func: Callable[[np.ndarray], float],
                     eps: float,
                     start: np.ndarray):
    n = len(start)
    x = start.copy()

    directions = np.eye(n)
    k = 1

    while True:
        displacements = []

        next_x = x.copy()
        for i in range(n):
            func_of_alpha = lambda alpha: func(next_x + alpha * directions[i])
            min_alpha = minimize_scalar(func_of_alpha).x

            displacements.append(directions[i] * min_alpha)
            next_x += min_alpha * directions[i]

        if np.linalg.norm(next_x - x) < eps:
            return next_x

        A = []
        for i in range(n):
            a_i = np.zeros(n)
            for j in range(i, n):
                a_i += displacements[j] * directions[j]
            A.append(a_i)

        new_directions = []
        for i in range(n):
            v = A[i]
            for j in range(len(new_directions)):
                proj = np.dot(A[i], new_directions[j]) * new_directions[j]
                v -= proj
            new_directions.append(v / np.linalg.norm(v))

        x = next_x.copy()

        k += 1



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


x_opt = minimize_with_rosenbrok_method(
    func=function,
    start=x0,
    eps=1e-3,
)

print(f"x_opt = {x_opt}")

print(f"f_opt = {function(x_opt)}")
