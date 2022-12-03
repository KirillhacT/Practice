def romanToInt():
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    awake_symbols = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }


    s = input()
    massive_incorrect = []
    sum = 0
    for i in range(len(s)):
        if i not in massive_incorrect:
            if i + 1 == len(s):
                sum += int(symbols[s[i]])
            else:
                if int(symbols[s[i]]) < int(symbols[s[i+1]]):
                    sum += awake_symbols[s[i] + s[i+1]]
                    massive_incorrect.append(i+1)
                    continue
                sum += int(symbols[s[i]])
    print(sum)

def romanToInt2():
    s = input()
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
print(romanToInt2())




