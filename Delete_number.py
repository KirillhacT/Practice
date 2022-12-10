def delete_number(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

print(delete_number([3, 2, 2, 3, 2, 3], 3))

# def remove_element(nums, val):
#     def key(num: int):
#         return 51 if num == val else num
#
#     nums.sort(key=key)
#     return len(nums) - nums.count(val)