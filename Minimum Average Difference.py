def min_average_difference(nums):
    min_average_difference = float("inf")
    left = 0
    right = 0
    s = sum(nums)
    res = 0
    for i, num in enumerate(nums):
        left += num
        right = s - left
        if i != len(nums) - 1:
            average = abs(left // (i + 1) - right // (len(nums)-i-1))
            if average < min_average_difference:
                min_average_difference = average
                res = i
        else:
            average = abs(left // (i + 1))
            if average < min_average_difference:
                res = i
    return res

nums = [0]
print(min_average_difference(nums))