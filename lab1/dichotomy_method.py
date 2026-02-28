from prettytable import PrettyTable
import math

def dichotomy(f, a, b, eps):

    table = PrettyTable()
    table.field_names = [
        "k", "a", "b", "l = b-a", "x1", "x2", "f(x1)", "f(x2)"
    ]

    k = -1

    while (b - a) > 2 * eps:
        k += 1

        x = (a + b) / 2
        x1 = x - eps / 2
        x2 = x + eps / 2

        f1 = f(x1)
        f2 = f(x2)

        table.add_row([
            k,
            round(a, 6),
            round(b, 6),
            round(b - a, 6),
            round(x1, 6),
            round(x2, 6),
            round(f1, 6),
            round(f2, 6)
        ])

        if f1 > f2:
            a = x1
        else:
            b = x2

    result_x = x
    result_f = f(result_x)

    print(table)
    print("\nрезультат:")
    print("x* =", round(result_x, 6))
    print("f(x*) =", round(result_f, 6))

    return result_x, result_f

def f(x):
    return x * math.exp(-x)


dichotomy(f, -2, 6, 0.1)
