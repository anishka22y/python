def two_sum(nums, target):
    num_index_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index_map:
            return [num_index_map[complement], i]
        num_index_map[num] = i

    return []  
nums = [3, 2, 4]
target = 6
output = two_sum(nums, target)
print(output)  
