l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1_len = len(l1)
l2_len = len(l2)
print(l1, l2)

num1 = 0
for i in range(len(l1)):
    num1 += (10 ** (l1_len - 1)) * l1[l1_len-1]
    l1_len -= 1

num2 = 0
for i in range(len(l2)):
    num2 += (10 ** (l2_len - 1)) * l2[l2_len-1]
    l2_len -= 1
sum = num1 + num2
print(sum)

n = len(str(sum))
massive = [0] * n
for i in range(n):
    num = sum % 10
    massive[i] = num
    sum //= 10
print(massive)












