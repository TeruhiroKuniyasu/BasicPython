from math import sin, pi

def integral(a, b, n, f):
    h = (b - a) / n
    S_current = 0

    for k in range(1, n):
        tmp = (h / 2) * (f(a + (k - 1) * h) + f(a + k * h))
        S_current = tmp + S_current
    return S_current

def f(x):
    return sin(x)
#ここで関数を変えることで対応可能

a = float(input("\naの値を入力: "))
b = float(input("bの値を入力: "))
n = int(input("分割数nの値を入力: "))
print("\n積分値：", integral(a, b, n, f))
    
