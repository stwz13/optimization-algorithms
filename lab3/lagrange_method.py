import sympy as sp

def lagrange_method(func, constraint, variables):

    lambda_var = sp.Symbol("lambda")

    L = func + lambda_var * constraint
    equations = [sp.diff(L, var) for var in variables]
    equations.append(constraint)

    solution_of_system = sp.solve(equations, variables+[lambda_var], dict=True)[0]

    opt_point = [solution_of_system[var] for var in variables]
    opt_value = func.subs(solution_of_system)

    return {
        "opt_point": opt_point,
        "opt_value": opt_value
    }


x1, x2 = sp.symbols("x1 x2")
func = x1- x2
constraint = 1.5*x1**2 + x2**2 - 3

opt_solution = lagrange_method(func, constraint, [x1, x2])
print(f"x_opt = {opt_solution["opt_point"]}")
print(f"f_opt = {opt_solution["opt_value"]}")
