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
a = 0
b = pi / 2
n = 50
print("\n(1)積分値：", integral(a, b, n, f = f1))

def f2(x):
    return 4 / (1 + x**2)
a = 0
b = 1
n = 100
print("\n(2)積分値：", integral(a, b, n, f = f2))

def f3(x):
    return pi**0.5 * exp(-x**2)
a = -100
b = -100
n = 1000
print("\n(3)積分値：", integral(a, b, n, f = f3))
