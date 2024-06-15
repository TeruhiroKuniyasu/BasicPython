from math import sin, pi

a = 0
b = pi / 2
h = (b - a) / 100

k = 1
S_current = 0

for k in range(1, 100 + 1):
    tmp = (h / 2) * (sin(a + (k - 1) * h) + sin(a + k * h))
    S_current = tmp + S_current

print(S = S_current)
    
