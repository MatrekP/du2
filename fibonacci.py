# Fibonacciho posloupnost pro n 0 az 20


def fibonacci(n):
    if n < 2:
        if n < 1:
            return 0
        else:
            return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(0,20):
    print(fibonacci(i))
