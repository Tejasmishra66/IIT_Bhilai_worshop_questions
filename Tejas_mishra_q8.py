def is_perfect(n):

    if n <= 1:
        return False
    divisors_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i and n // i != n:
                divisors_sum += n // i
    
    return divisors_sum == n

def is_perfect_simple(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    
    return divisors_sum == n

print(is_perfect(6)) 
print(is_perfect(28))  
print(is_perfect(12))
