def make_abc():
    result = "a, b, c"
    return result

print("Demonstrate make abc")
print(make_abc())


def equal_edges(items):
    first = items[0]
    last = items[-1]
    result = first == last 

    if first == last:
        return True
    else:
        return False
    
print("Demonstrate equal_edges")
print("[1, 2, 1] ->", equal_edges([1, 2, 1]))


def all_the_same(list1,):
    first1, middle1, last1 = list1

    if first1 == middle1 == last1:
        return True
    else:
        return False
    
print("Demonstrate all_the_same")
print("[1, 3, 2] = ", all_the_same([1, 3, 2]))
print("[1, 1, 1] = ", all_the_same([1, 1, 1]))


def increasing(list1):
    first1, middle1, last1 = list1

    first1 = list1[0]
    middle1 = list1[1]
    last1 = list1[2]

    if first1 == middle1 == last1:
        return True
    else:
        return False
    
print("Demonstrate increasing")
print("[1, 1, 1] = ", increasing([1, 1, 1]))
print("[5, 1, 2] = ", increasing([5, 1, 2]))


def all_true(list1):
    word1, word2, word3 = list1

    word1 = list1[0]
    word2 = list1[1]
    word3 = list1[2]

    if word1 == word2 == word3:
        return True
    else:
        return False
    
print("Demonstrate all_true")
print("[true, true, true] = ", all_true([True, True, True]))
print("[true, true, false] = ", all_true([True, True, False]))


def mostly_true(list1):
    word1, word2, word3 = list1

    word1 = list1[0]
    word2 = list1[1]
    word3 = list1[2]

    if word1 == True and word2 == True and word3 == False:
        return True
    elif word1 == True and word2 == False and word3 == True:
        return True
    elif word1 == False and word2 == False and word3 == True:
        return False
    elif word1 == False and word2 == True and word3 == True:
        return True
    elif word1 == False and word2 == True and word3 == False:
        return False
    
print("Demonstrate mostly_true")
print("[true, true, false] = ", mostly_true([True, True, False]))
print("[false, false, true] = ", mostly_true([False, False, True]))


def make_copy(list1):
    word1, word2, word3 = list1
    
    word1 = list1[0]
    word2 = list1[1]
    word3 = list1[2]
    return list1

print("Demonstrate make_copy")
print("[5, 6, 1] = ",  make_copy([5, 6, 1]))


def repeat_thrice(list1):
    word1 = max(list1)
    return [word1, word1, word1]

print("Demonstrate repeat_thrice")
original_list = [1]
new_list = repeat_thrice(original_list)
print("original list: ", original_list)
print("new list: ", new_list)


def make_reversed_copy(list1):
    word1, word2, word3 = list1

    word3 = list1[0]
    word2 = list1[1]
    word1 = list1[2]

    return [word1, word2, word3]


print("Demonstrate make_reversed_copy")
original_list = [1, 2, 3]
new_list = make_reversed_copy(original_list)
print("original list: ", original_list)
print("new list: ", new_list)



def reverse_in_place(list1):
    word1, word2, word3 = list1


    word3 = list1[0]
    word1 = list1[2]

    return [word1, word2, word3]
    
print("Demonstrate reverse_in_place")
original_list = [1, 4, 3]
new_list = reverse_in_place(original_list)
print("original list: ", original_list)
print("new list: ", new_list)
