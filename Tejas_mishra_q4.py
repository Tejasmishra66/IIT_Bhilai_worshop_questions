def is_palindrome(s):

    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("Madam"))
print(is_palindrome("Step on no pets")) 
print(is_palindrome("Hello, World!"))
