
def fib(n):
    if n < 3:
        return 1

    a = fib(n-1) + fib(n-2)
    return a

print(fib(5))