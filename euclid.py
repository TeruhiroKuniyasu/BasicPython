def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def relatively_prime(a, b):
    bool = False
    while b != 0:
        a, b = b, a % b
    if a == 1:
        bool = True
    return bool

a = int(input("\na の値を入力: "))
b = int(input("b の値を入力: "))

print("\nGCD = ", GCD(a, b))
print("Relatively prime: ", relatively_prime(a, b))
