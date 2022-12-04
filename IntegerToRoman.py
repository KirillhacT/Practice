num = int(input())
symbols = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
    4: "IV",
    9: "IX",
    40: "XL",
    90: "XC",
    400: "CD",
    900: "CM"
}
hash = {}
solt = 0
for i in range(len(str(num))):
    current = (num % 10) * 10 ** solt
    if current != 0:
        hash[i] = current
    solt += 1
    num //= 10
N = len(hash)
string = ""
for i in hash:
    if hash[i] not in symbols:
        max = 0
        min = 0
        for j in symbols:
            if j > max and j < hash[i]:
                max = j
        for k in symbols:
            if k > min and max + k <= hash[i]:
                min = k
        sum = max
        string2 = f"{symbols[max]}"
        while sum != hash[i]:
            sum += min
            string2 += symbols[min]
        string = string2 + string
    else:
        string = symbols[hash[i]] + string
print(string)