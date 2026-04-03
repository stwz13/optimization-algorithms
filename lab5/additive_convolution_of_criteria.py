from scipy.optimize import minimize
def additive_convolution_method(funcs_list, weights, x0):

    def objective(x):
        return sum(w * f(x) for w, f in zip(weights, funcs_list))

    res = minimize(objective, x0, method='BFGS')


    return res.x