def fibonacci(n):

    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a + b
    return b
    
print(fibonacci(1)) 
print(fibonacci(7)) 
print(fibonacci(10))
