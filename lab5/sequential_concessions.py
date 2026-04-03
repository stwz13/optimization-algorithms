import numpy as np
from scipy.optimize import minimize


def minimize_with_sequential_concessions(funcs, x0, concessions):
    curr_x = x0

    constraints = []

    for i in range(len(funcs)):
        target_f = funcs[i]

        res = minimize(target_f, curr_x, method="SLSQP", constraints=constraints)

        target_f_min = res.fun
        curr_x = res.x

        if i < len(concessions):
            delta = concessions[i]

            limit = target_f_min + delta

            constraints.append({
                'type': 'ineq',
                'fun': lambda x, f_to_constrain=target_f, L=limit: L - f_to_constrain(x)
            })

    return curr_x

centers = [(2, 5), (-4, -1), (5, -2)]

def f(i, x):
    b, d = centers[i]
    return (x[0] - b)**2 + (x[1] - d)**2

x0 = np.array([0, 0])

