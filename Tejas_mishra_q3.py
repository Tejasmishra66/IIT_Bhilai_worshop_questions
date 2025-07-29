def trailing_zeros(n):
    
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    
    return count
print(trailing_zeros(5))
print(trailing_zeros(100))
print(trailing_zeros(0))
