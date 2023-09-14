def add_binary(a, b):
    binary = []
    q, r = divmod(a + b, 2)
    binary.append(r)
    while q > 0:
        q, r = divmod(q, 2)
        binary.append(r)

    return "".join([str(i) for i in list(reversed(binary))])


def add_binary_1(a, b):
    q, r = divmod(a + b, 2)
    s = str(r)
    while q > 0:
        q, r = divmod(q, 2)
        s += str(r)

    return "".join(reversed(s))


def add_binary_2(a, b):
    return "{:b}".format(a + b)


def add_binary_3(a, b):
    return bin(a + b)[2:]


print(add_binary_3(10, 3))  # 1101

print("{:b}".format(13))  # https://www.w3schools.com/python/ref_string_format.asp
