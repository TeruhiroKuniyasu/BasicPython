a = int(input("\naの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
is_prime_a = True
is_prime_b = True

if a <= 1:
    is_prime_a = False
else:
    for i in range(2, int(a)):
        if a %i == 0:
            is_prime_a = False
            break

if is_prime_a == True:
    print("\n'a' is a prime number.")
else:
    print("\n'a' is not a prime number.")

if b <= 1:
    is_prime_b = False
else:
    for i in range(2, int(b)):
        if b %i == 0:
            is_prime_b = False
            break

if is_prime_b == True:
    print("'b' is a prime number.\n")
else:
    print("'b' is not a prime number.\n")
