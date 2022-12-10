# def binary_search(nums, target):
#     low = 0
#     high = len(nums)-1
#     while low <= high: #!
#         middle = (high + low) // 2
#         current = nums[middle]
#         if current == target:
#             return middle
#         elif current > target:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return -1
#
# nums = [7]
# target = 7
# print(binary_search(nums, target))

# def first_bad_version(n):
#     first_n = 0
#     last_n = n
#     min_bad = 999999
#     while first_n <= last_n:
#         middle = (first_n + last_n) // 2
#         if not isBadVersion(middle):
#             first_n = middle + 1
#         else:
#             if min_bad > middle:
#                 min_bad = middle
#             last_n = middle - 1
#     return first_n
#
#
#
# def isBadVersion(number):
#     if number >= bad:
#         return True
#     return False
#
# n = int(input())
# bad = int(input())
#
# print(first_bad_version(n))


# def insert_search(nums, target):
#     low = 0
#     high = len(nums)-1
#     while low <= high:
#         middle = (high + low) // 2
#         current = nums[middle]
#         if current == target:
#             return middle
#         elif current > target:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return low
#
# nums = [1,3,5,6]
# target = 2
# print(insert_search(nums, target))






