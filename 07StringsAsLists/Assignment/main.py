def is_alliteration(list1, list2):
    firstletter = list1[0]
    if list2[0] == firstletter:
        return True
    return False

print("Demonstrate is_alliteration")
print("apple, ant = ", is_alliteration("apple", "ant"))
print("banana, cat = ", is_alliteration("banana", "cat"))

def count_vowels(list):
    count = 0
    for vowels in list:
        if vowels in ["a", "e", "i", "o", "u"]:
            count = count + 1
    return count

print("Demonstrate count_vowels")
print("apple = ", count_vowels("apple"))
print("elephant = ", count_vowels("elephant"))

def count_numbers(string):
    count = 0
    for character in string:
        if character in "123456789":
            count = count + 1
    return count

print("Demonstrate count_numbers")
print("789ghi = ", count_numbers("789ghi"))
print("123abc = ", count_numbers("123abc"))

def count_target_numbers(word1, word2):
    count = 0
    for letter in word1:
        if letter == word2:
            count = count + 1
    return count

print("Demonstrate count_target_numbers")
print("apple, a = ", count_target_numbers("apple", "a"))
print("banana, a = ", count_target_numbers("banana", "a"))


def in_alphabetical_order(string):
    previous = "a"
    for letter in string:
        if letter >= previous and letter <= previous:
            return False
    return True


print("Demonstrate in_alphabetical_order")
# bin -> true
# apple -> false
print(in_alphabetical_order("bin"))
print(in_alphabetical_order("apple"))
print(in_alphabetical_order("abc"))

def alternate_case(string):
    result = ""
    next_upper = True
    for letter in string:
        if letter == string:
            next_upper = True
        elif next_upper == True:
            letter.upper()
            next_upper = False
        elif next_upper == False:
            next_upper == True
        elif next_upper == True:
            letter.upper()
            next_upper = False
        elif next_upper == False:
             next_upper == True
        elif next_upper == True:
            letter.upper()
            next_upper = False

print("Demonstrate alternate_case")
print(alternate_case("python"))