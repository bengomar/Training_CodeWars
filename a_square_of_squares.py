def is_square(n):
    n_square = n**0.5
    search = str(n_square).find(".")
    return str(n_square)[search:] == ".0"


def is_square_1(n):
    return n >= 0 and (n**0.5) % 1 == 0


def is_square_2(n):
    num = n**0.5
    return (num * num) == n


print(is_square(26))
print(is_square(25))

print(is_square_1(-1))
print(is_square_1(25))

print(is_square_2(-1))
print(is_square_2(25))
