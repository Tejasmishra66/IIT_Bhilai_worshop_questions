def swap(a, b):
    a, b = b, a
    return (a, b)

def swap_arithmetic(a, b):
    a = a + b
    b = a - b 
    a = a - b 
    return (a, b)

def swap_xor(a, b):
    if a != b:
        a = a ^ b
        b = a ^ b
        a = a ^ b 
    return (a, b)

print(swap(3, 5))  
print(swap(-1, 10))  
print(swap(0, 0))    
