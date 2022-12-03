def check_number_is_palindrome(x: int) -> bool:
    hash = {}
    count = 0
    if x == 0:
        return True
    while x > 0:
        tmp = x % 10
        hash[count] = tmp
        count += 1
        x //= 10
    if hash == {}:
        return False
    min_count = 0
    max_count = count - 1
    for i in range(count//2):
        if hash[min_count] != hash[max_count]:
            return False
        min_count += 1
        max_count -= 1
    return True
print(check_number_is_palindrome(0))
