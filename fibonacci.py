def fibonacci(num):
    a, b = 1, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return a

fib50 = fibonacci(50)
print(fib50)