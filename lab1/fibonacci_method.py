from typing import Callable
import prettytable as pt
import time


def minimize_with_fibonacci_method(function_to_minimize: Callable[[float], float],
                                   a: float, b:float,
                                   eps: float,
                                   print_process_of_solution: bool = False):

    table = pt.PrettyTable()

    table.field_names = ["number_of_iteration", "a", "b", "l",
                         "x1", "x2",
                         "f1", "f2"]
    table.float_format = ".5"

    start = time.time()

    fibonacci_array = [1, 1]
    n = len(fibonacci_array) - 1

    while not (fibonacci_array[n] >= (b-a) / eps):
        fibonacci_array.append(fibonacci_array[-1] + fibonacci_array[-2])
        n += 1

    print(n)

    l = b - a

    while n > 2:
        x1 = a + fibonacci_array[n-1] / fibonacci_array[n] * l
        x2 = b - fibonacci_array[n-1] / fibonacci_array[n] * l

        f1 = function_to_minimize(x1)
        f2 = function_to_minimize(x2)

        table.add_row([len(fibonacci_array) - n - 1, a, b, l,
                       x1, x2,
                       f1, f2])

        if f1 > f2:
            b = x1
            f1 = f2
            x1 = x2
            l = b - a
            x2 = b - fibonacci_array[n-2]/fibonacci_array[n-1] * l
        else:
            a = x2
            f2 = f1
            x2 = x1
            l = b - a
            x1 = a + fibonacci_array[n - 2] / fibonacci_array[n - 1] * l

        n = n - 1

    x_min = (a+b) / 2
    f_opt = function_to_minimize(x_min)

    end = time.time()
    exe_time = end - start
    table.add_row([len(fibonacci_array) - n - 1, a, b, l, "", "", "", ""])
    if print_process_of_solution:
        print(f"Аccuracy: {eps}")
        print(table)
        print(f"x_min: {x_min}")
        print(f"f_opt: {function_to_minimize(x_min):.5f}")
        print(f"execution time: {exe_time:.5f}")

    return x_min, f_opt
