from scipy.optimize import minimize


def additive_convolution_method(funcs, weights, x0):
    objective = lambda x: sum(w * f(x) for w, f in zip(weights, funcs))

    res = minimize(objective, x0, method="SLSQP")
    return res.x

