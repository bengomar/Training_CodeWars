def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


result = descending_order(123456789)
print(result)
