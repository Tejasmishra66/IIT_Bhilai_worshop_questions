def count_letters(text):

    vowels = {'a', 'e', 'i', 'o', 'u'}

    vowel_count = 0
    consonant_count = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)
    
print(count_letters("Data Science"))
print(count_letters("IIT Bhilai"))
print(count_letters("1234!"))  
