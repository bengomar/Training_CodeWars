# input --> 9119
#
# output --> 811181
# because 9^2 is 81 and 1^2 is 1


def squareDigit(num):
    number = ""
    for i in str(num):
        number += str(int(i) ** 2)
    return int(number)


def squareEveryDigit(number):
    return int("".join(str(int(i) ** 2) for i in str(number)))


def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x) ** 2)
    return int(ret)


print(squareDigit(765))
print(squareEveryDigit(765))
print(square_digits(765))
