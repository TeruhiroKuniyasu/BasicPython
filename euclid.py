def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def relatively_prime(a, b):
    is_relatively_prime = False
    if GCD(a, b) == 1:
        return True

a = int(input("\na の値を入力: "))
b = int(input("b の値を入力: "))

print("\nGCD = ", GCD(a, b))
print("Relatively prime: ", relatively_prime(a, b))
