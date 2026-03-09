import numpy as np
from typing import Callable



def minimize_with_hook_jeeves_method(
        func: Callable[[np.ndarray], float],
        x0: np.ndarray,
        step_vector: np.ndarray,
        step_reduction: float = 0.1,
        eps: float = 1e-3
):
    k = 0

    last_x = x0.copy()
    last_z = func(x0)

    while not np.linalg.norm(step_vector) < eps:
        x_new = exploratory_search(func, last_x, step_vector)
        z_new = func(x_new)

        if z_new < last_z:
            x_p = x_new + (x_new - last_x)
            curr_x = exploratory_search(func, x_p, step_vector)
            curr_z = func(curr_x)

            if curr_z < z_new:
                last_x = curr_x
                last_z = curr_z

            else:
                last_x = x_new
                last_z = z_new

        else:
            step_vector *= step_reduction

    return last_x


def exploratory_search(
        func: Callable[[np.ndarray], float],
        x0: np.ndarray,
        step_vector: np.ndarray,):
    last_y = x0.copy()
    last_z = func(x0)
    n = len(x0)
    k = 0

    for i in range(n):
        base_vector = np.zeros(n)
        base_vector[i] = 1
        step_size = step_vector[i]

        y_k = last_y + step_size * base_vector
        z_k = func(y_k)

        if z_k < last_z:
            last_y = y_k
            last_z = z_k


        y_k = last_y - step_size * base_vector
        z_k = func(y_k)

        if z_k < last_z:
            last_y = y_k
            last_z = z_k

    return last_y

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

x_opt = minimize_with_hook_jeeves_method(
    func=function,
    x0=x0,
    step_vector=step_vector,
    step_reduction=0.5,
    eps=1e-2,
)

print(x_opt)