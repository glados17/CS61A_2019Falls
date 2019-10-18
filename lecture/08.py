# Decorators

def trace1(fn):
    """Return a function equivalent to fn that also prints trace output.

    fn -- a function of one argument.
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x*x

@trace1
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total

# Implementing Functions

def remove(n, digit):
    """Return all digits of N that are not DIGIT, for DIGIT less than 10.

    >>> remove(231, 3) 
    21
    >>> remove(240132, 2)
    4013
    """
    kept, digits = 0, 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept / 10 + last
            digits = digits + 1
    return round(kept * 10 ** (digits - 1))


def remove2(n, digit):
    """Return all digits of N that are not DIGIT, for DIGIT less than 10.

    >>> remove2(231, 3) 
    21
    >>> remove2(240132, 2)
    4013
    """
    kept, digits = 0, 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * 10 ** digits
            digits = digits + 1
    return kept
