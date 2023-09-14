def duplicateEncoder(word):
    string = ""
    word = word.lower()
    for i in word:
        n = word.count(i)
        if n > 1:
            i = ")"
        else:
            i = "("
        string += i
    return string


print(duplicateEncoder("Success"))
