def Reverse_integer(x) -> int:
    MAX_NUM = 2**31 - 1
    MIN_NUM = -2**31
    x = str(x)
    if x[0] == "-":
        minus = "-"
        x = x.replace("-", "")
    else:
        minus = ""
    new_x = x[::-1]
    new_x = minus + new_x

    index = 0
    for i in range(len(new_x)):
        if new_x[i] == "0":
            index = i
        else:
            break
    new_x = int(new_x[index:])
    if MIN_NUM < new_x < MAX_NUM:
        return new_x
    return 0
print(Reverse_integer(1534236469))


def reverse(self, x: int) -> int:
    is_negative = False
    if x < 0:
        is_negative = True
        x = x * -1

    reverse_number = 0
    while x:
        n = x % 10
        x = x // 10
        reverse_number = reverse_number * 10 + n

    if is_negative:
        reverse_number = reverse_number * -1

    MIN_VALUE = 2 ** 31 * (-1)
    MAX_VALUE = 2 ** 31 - 1
    if reverse_number > MAX_VALUE or reverse_number < MIN_VALUE:
        return 0
    return reverse_number