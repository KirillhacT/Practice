nums = [4, 1, 2, 3, 5]
target = 8

# for i in nums:
#     for j in nums:
#         if i + j == target:
#             print(i, j)

hash = {}
for i in range(len(nums)):
    hash[nums[i]] = i
print(hash)

for i in range(len(nums)):
    new = target - nums[i]
    if new in hash and hash[new] != i:
        print(hash[new], i)
        exit()





