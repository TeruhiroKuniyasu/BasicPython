def prime(n):
    bool = True

    if n <= 1:
        bool = False
    else:
        for i in range(2, int(n**0.5 + 1)):
            if n %i == 0:
                bool = False
                break
    return bool

n = int(input("\nnの値を入力: "))
print(prime(n))


