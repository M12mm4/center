def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    else :
        n = max(len(str(x)), len(str(y)))
        half = n // 2
        a = x // (10**half)
        b = x % (10**half)
        c = y // (10**half)
        d = y % (10**half)
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ac_bd = karatsuba(a+b, c+d) - ac - bd
        return ac * (10**(2 * half)) + (ac_bd * (10**half)) + bd

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba(x, y))