def arrayPairSum(nums):
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += nums[i]
    return sum

print(arrayPairSum([1, 4, 3, 2, 5, 7]))