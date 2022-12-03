string = input()
hash = {
    "(": ")",
    "[": "]",
    "{": "}"
}
new_s = ""
list_uncorrect_indexes = []
for i in range(len(string)):
        if string[i] in hash:
            current = hash[string[i]]
            for j in range(i, len(string)):
                if j not in list_uncorrect_indexes:
                    if string[j] == current:
                        list_uncorrect_indexes.append(j)
                        new_s += string[i] + string[j]
                        break
print(new_s)
# if string[sk] in hash:
# if sk not in list_uncorrect_indexes: