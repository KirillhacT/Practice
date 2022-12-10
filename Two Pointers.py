def Squares_of_a_Sorted_Array(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return sorted(nums)

nums = [-4, -1, 0, 3, 10]
print(Squares_of_a_Sorted_Array(nums))