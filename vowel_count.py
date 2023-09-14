def get_count(sentence):
    sentence = sentence.lower()
    nb_vowels = 0

    for v in list("aeiou"):
        if v in sentence:
            nb_vowels += sentence.count(v)
    return nb_vowels


def getCount(inputStr):
    return sum(1 for letter in inputStr if letter in "aeiouAEIOU")


string = "Aujourd'hui c'est Mercredi!"
print(get_count(string))
print(getCount(string))
