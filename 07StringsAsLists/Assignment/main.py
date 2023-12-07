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

def count_numbers(list):
    count = 0
    for numbers in list:
        if numbers > 1:
            count = count + numbers
    return count

print("Demonstrate count_numbers")
print("789ghi = ", count_numbers("789ghi"))