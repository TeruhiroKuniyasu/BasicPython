def prime(n):
    is_prime = True

    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5 + 1)):
            if n %i == 0:
                return False
        return True

n = int(input("\nnの値を入力: "))
print(prime(n))


