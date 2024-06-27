from math import sin, pi, exp

def integral(a, b, n, f):
    a = 0
    b = 1
    n = 100 
    h = (b - a) / n
    S_current = 0

    for k in range(1, n + 1):
        tmp = (h / 2) * (f(a + (k - 1) * h) + f(a + k * h))
        S_current = tmp + S_current
        
    return S_current

def f1(x):
    return sin(x)
print("\n(1)積分値：", integral(0, pi/2, 50, f = f1))

def f2(x):
    return 4 / (1 + x**2)
print("\n(2)積分値：", integral(0, 1, 100, f = f2))

def f3(x):
    return pi**0.5 * exp(-x**2)
print("\n(3)積分値：", integral(-100, 100, 1000, f = f3))
