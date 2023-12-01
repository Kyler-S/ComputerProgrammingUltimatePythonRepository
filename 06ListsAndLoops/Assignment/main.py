def count_failing_grades(list):
    count = 0
    for numbers in list:
        if numbers in ["60%", "55%", "50%", "45%", "40%", "35%", "30%", "25%", "20%", "15%", "10%"]:
            count = count + 1


    return count

inputlist = ["60%", "55%", "50%", "80%", "65%"]
returnvalue = count_failing_grades(inputlist)
print("This many people have failing grades")
print(returnvalue)


def count_act_score(list):
    count = 0
    for numbers in list:
        if numbers in ["65%", "70%", "75%", "80%", "85%", "90%", "95%", "100%"]:
            count = count + 1


    return count

inputlist = ["75%", "80%", "55%", "65%", "10%", "90%", "95%", "100%", "50%", "60%"]
returnvalue = count_act_score(inputlist)
print("This many people have a valid ACT score")
print(returnvalue)


def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number

    return total

inputlist = [4, 3, 6, 9]
returnvalue = number_sum(inputlist)
print("This is the total")
print(returnvalue)


def average_act_score(list):
    total = 0
    count = 0
    for number in list:
        if number <= 35 and number > 1:
            total = total + number
            count = count + 1
        
    return total / count
    


inputlist = [-1, 100, 35, 30, 25, 55, 104]
returnvalue = average_act_score(inputlist)
print("This is the average ACT score")
print(returnvalue)


def all_true(list):
    for boolean in list:
    return True

print("Demonstrate all_true")
print("[true, true, false] = ", all_true([True, True, False]))
print("[true, true, true] = ", all_true([True, True, True]))

def any_true(list):
    for boolean in list:
        if boolean in [True]:
            return True
    return False

print("Demonstrate any_true")
print("[false, false, true] = ", any_true([False, False, True]))
print("[false, false, false] = ", any_true([False, False, False]))

def mostly_true(list):
    word1, word2, word3 = list

    word1 = list[0]
    word2 = list[1]
    word3 = list[2]

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
