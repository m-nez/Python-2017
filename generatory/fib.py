# Copyrigth (C) 2017 Michał Nieznański

def x2(x):
    """
    >>> x2(4)
    16
    >>> x2(5)
    26
    """
    return x*x

def fib(n):
    a, b = 1, 0
    for _ in range(n):
        yield a
        a, b = a + b, a

print(*fib(10), sep=", ")
