def Squares_of_a_Sorted_Array(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return sorted(nums)

nums = [-4, -1, 0, 3, 10]
# print(Squares_of_a_Sorted_Array(nums))

def rotate_array(nums, k):
    cou = len(nums)-k
    num1 = nums[:cou]
    num2 = nums[cou:]
    return num2 + num1

numsik = [-1,-100,3,99]
print(rotate_array(numsik, 2))






















