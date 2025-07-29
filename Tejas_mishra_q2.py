def is_armstrong(n):

    str_n = str(n)
    num_digits = len(str_n)
    digit_sum = sum(int(digit) ** num_digits for digit in str_n)
    return digit_sum == n
print(is_armstrong(153))
print(is_armstrong(370))
print(is_armstrong(123))
