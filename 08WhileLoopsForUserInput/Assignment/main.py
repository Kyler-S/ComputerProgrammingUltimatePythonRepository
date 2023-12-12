print("Your on number_guesser")
import random
def number_guesser():
    secretnumber = random.randint(1, 10)
    while True:
        try:
            guess = int(input())
        except ValueError:
            print("not a valid number")
            continue

        if guess == secretnumber:
            print("You guessed the right one")
            break 
        elif guess > secretnumber:
            print("Too high")
        else:
            print ("Too low")

number_guesser()

print("Your on number_guesser_with_lives")
import random
def number_guesser_with_lives(lives):
    secretnumber = random.randint(1, 10)
    lives = 3
    while lives > 0:
        try:
            guess = int(input())
        except ValueError:
            print("not a valid number")
            continue

        if guess == secretnumber:
            print("You guessed the right one")
            break 
        elif guess > secretnumber:
            print("Too high")
        else:
            print ("Too low")
            
        lives -= 1
        print(f"You have {lives} {'life' if lives == 1 else 'lives'} remaining.")

    if lives == 0:
        print(f"Sorry, you're out of lives")

number_guesser_with_lives("lives=") 


print("You are now on vending_machine")
def vending_machine():
    cost = 50
    amount_due = cost
    print(f"Amount due: {amount_due} cents")
    while amount_due > 0:
        coin = int(input("Enter a coin (25, 10, or 5): "))
        if coin in [25, 10, 5]:
            amount_due -= coin
            print(f"Amount due: {amount_due} cents")
        else:
            print("Invalid coin. Please enter a valid coin.")
    change = -amount_due
    print(f"Here is your change: {change} cents")

vending_machine()
