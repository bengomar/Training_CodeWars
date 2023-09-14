def create_phone_number(n):
    if len(n) == 10:
        return f"{'(' + ''.join([str(a) for a in n[0:3]]) + ')'} {''.join([str(a) for a in n[3:6]])}-{''.join([str(a) for a in n[6:10]])}"
    else:
        return "the must have ten digits !"


def create_phone_number_2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number_3(n):
    n = "".join(map(str, n))
    return "(%s) %s-%s" % (n[:3], n[3:6], n[6:])


result = create_phone_number(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 1]
)  # => returns "(123) 456-7890"
print(result)
