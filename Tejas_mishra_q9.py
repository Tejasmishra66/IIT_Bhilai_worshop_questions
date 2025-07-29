def is_isogram(s):
    letters = [char.lower() for char in s if char.isalpha()]

    return len(letters) == len(set(letters))
    
def is_isogram_alternative(s):
    seen = set()
    
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in seen:
                return False
            seen.add(char_lower)
    
    return True

print(is_isogram("Machining")) 
print(is_isogram("Algorithm")) 
print(is_isogram("Dermatoglyphics"))
