# Faktorial pro n 1 az 20


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(1,20):
    print(factorial(i))
