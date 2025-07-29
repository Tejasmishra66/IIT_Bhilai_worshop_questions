def second_largest(nums):
    if not nums:
        return None
    unique_nums = set(nums)
    if len(unique_nums) < 2:
        return None
    sorted_unique = sorted(unique_nums, reverse=True)
    return sorted_unique[1]

def second_largest_iterative(nums):
    if not nums:
        return None
    
    largest = second = None
    
    for num in nums:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    
    return second

print(second_largest([2, 5, 1, 4, 5])) 
print(second_largest([7, 7, 7]))
print(second_largest([10, 9, 8]))
