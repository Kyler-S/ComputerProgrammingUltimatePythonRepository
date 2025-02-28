def count_failing_grades(list):
    count = 0
    for numbers in list:
        if numbers < 60:
            count = count + 1


    return count

inputlist = [50, 70, 80]
returnvalue = count_failing_grades(inputlist)
print("This many people have failing grades")
print(returnvalue)


def count_act_score(list):
    count = 0
    for numbers in list:
        if numbers <= 36 and numbers >= 1:
            count = count + 1


    return count

inputlist = [36, 35, 1, 0, 37]
returnvalue = count_act_score(inputlist)
print("This many people have a valid ACT score")
print(returnvalue)


def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number

    return total

inputlist = [100, 200, 300, 400, 500, 600, 700]
returnvalue = number_sum(inputlist)
print("This is the total")
print(returnvalue)


def average_act_score(list):
    total = 0
    count = 0
    for number in list:
        if number <= 36 and number >= 1:
            total = total + number
            count = count + 1
        
    if count == 0:
        return None
    
    return total / count
    


inputlist = [36, 35, 1, 0, 37]
returnvalue = average_act_score(inputlist)
print("This is the average ACT score")
print(returnvalue)


def all_true(list):
    for boolean in list:
        if boolean in [False]:
            return False
    return True


print("Demonstrate all_true")
print("true, false, true = ", all_true([True, False, True]))
print("true, true, true = ", all_true([True, True, True]))

def any_true(list):
    for boolean in list:
        if boolean in [True]:
            return True
    return False

print("Demonstrate any_true")
print("true, false, false = ", any_true([True, False, False]))
print("false, false, false = ", any_true([False, False, False]))

def mostly_true(list):
    for boolean in list:
        if boolean in [True, True]:
            return True
    return False

print("Demonstrate mostly_true")
print("false, false, false = ", mostly_true([False, False, False]))
print("true, true, true, false, flase = ", mostly_true([True, True, True, False, False]))


def has_vowels(list):
    for letter in list:
        if letter in ["a", "e", "i", "o", "u"]:
            return True
    return False

print("Demonstrate has_vowels")
print("a, b, c = ", has_vowels(["a", "b", "c"]))
print("d, e, f = ", has_vowels(["d", "e", "f"]))


def all_the_same(list):
    first = list[0]
    for num in list:
        if num != first:
            return False
    return True

print("Demonstrate all_the_same")
print("1, 1, 1 = ", all_the_same([1, 1, 1]))
print("1, 2, 3 = ", all_the_same([1, 2, 3]))


def increasing(list):
    previous = -9999999999999999
    for num in list:
        if num <= previous:
            return False
        previous = num
    return True
    
print("Demonstrate increasing")
print("1, 2, 3 = ", increasing([1, 2, 3]))
print("3, 2, 1 = ", increasing([3, 2, 1]))
print("1, 2, 3, 2 = ", increasing([1, 2, 3, 2]))


def is_incrementing(list):
    previous = list[0]-1
    for num in list:
        if num == previous+1:
            pass
        else:
            return False
        previous = num
    return True
    
print("Demonstrate is_incrementing")
print("1, 2, 3 = ", is_incrementing([1, 2, 3]))
print("1, 3, 5 = ", is_incrementing([1, 3, 5]))
print("1, 2, 3, 4, 5 = ", is_incrementing([1, 2, 3, 4, 5]))
print("2, 3, 4, 6, 7 = ", is_incrementing([2, 3, 4, 6, 7]))

def has_adjacent_repeat(list):
    for num in range(len(list) - 1):
        if list[num] == list[num + 1]:
            return True
    return False

print("Demonstrate has_adjacent_repeat")
print("1, 2, 2, 3 = ", has_adjacent_repeat([1, 2, 2, 3]))
print("1, 2, 3, 4 = ", has_adjacent_repeat([1, 2, 3, 4]))

def sum_with_skips(list):
    total = 0
    ignoring = False
    for num in list:
        if num == -1:
            ignoring = not ignoring
        elif not ignoring:
            total = total + num
    return total

print("Demonstrate sum_with_skips")
print("1, 2, 3, -1, 4, 5, 6, -1, 7 = ", sum_with_skips([1, 2, 3, -1, 4, 5, 6, -1, 7]))
print("1, -1, 2, -1, 3 = ", sum_with_skips([1, -1, 2, -1, 3]))