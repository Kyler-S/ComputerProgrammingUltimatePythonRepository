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