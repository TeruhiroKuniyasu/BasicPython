a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
r = 1

if a > b:
    while r != 0:
        r = a %b
        if r != 0:
            a,b = b,r    
    GCD = b
else:
    while r != 0:
        r = b %a
        if r != 0:
            b,a = a,r
    GCD = a

print("GCD = ", GCD)
