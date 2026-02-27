from typing import Callable
import prettytable as pt
import time

def minimize_with_golden_ratio_method(function_to_minimize: Callable[[float], float],
                                   a: float, b:float,
                                   eps: float,
                                   print_process_of_solution: bool = False):
    table = pt.PrettyTable()

    table.field_names = ["number_of_iteration", "a", "b", "l",
                         "x1", "x2",
                         "f1", "f2"]
    table.float_format = ".5"

    const_tao = 0.618

    start = time.time()
    number_of_iteration = 0
    l = b - a
    while l > eps:
        x1 = a + l * const_tao
        x2 = b - l * const_tao

        f1 = function_to_minimize(x1)
        f2 = function_to_minimize(x2)

        table.add_row([number_of_iteration, a, b, l,
                       x1, x2,
                       f1, f2])

        if f1 > f2:
            b = x1
            f1 = f2
            x1 = x2
            l = b - a
            x2 = b - l * const_tao
            f2 = function_to_minimize(x2)
        else:
            a = x2
            f2 = f1
            x2 = x1
            l = b - a
            x1 = a + l * const_tao
            f1 = function_to_minimize(x1)
        number_of_iteration+=1

    x_min = (a + b) / 2
    f_opt = function_to_minimize(x_min)
    end = time.time()

    exe_time = end - start
    table.add_row([number_of_iteration, a, b, l, "", "", "", ""])

    if print_process_of_solution:
        print(f"Аccuracy: {eps}")
        print(table)
        print(f"x_min: {x_min}")
        print(f"f_opt: {function_to_minimize(x_min):.5f}")
        print(f"execution time: {exe_time:.5f}")

    return x_min, f_opt