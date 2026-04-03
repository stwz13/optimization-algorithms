from scipy.optimize import minimize

def minimize_with_discriminant_method(obj_dict, constr_dict, x0):
    objective = lambda x: sum(weight * f(x) for f, weight in obj_dict.items())

    cons = []

    for f, limit in constr_dict.items():
        cons.append({
            "type": "ineq",
            "fun": lambda x, f_local=f, L_local=limit: L_local - f_local(x)
        })

    res = minimize(objective, x0, method="SLSQP", constraints=cons)

    return res.x


