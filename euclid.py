def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

print("GCD = ", GCD(a, b))
