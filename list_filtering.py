def filter_list(lst):
    ls = []
    for i in lst:
        try:
            if i - i == 0:
                ls.append(i)
        except TypeError:
            continue
    return ls


def filter_list_1(lst):
    return [i for i in lst if not isinstance(i, str)]


def filter_list_2(lst):
    return [x for x in lst if type(x) is not str]


result = filter_list_1([1, 2, "a", "b"])
result_2 = filter_list_2([1, "a", "b", 0, 15])
result_3 = filter_list([1, 2, "aasf", "1", "123", 123])
print(result)
print(result_2)
print(result_3)
