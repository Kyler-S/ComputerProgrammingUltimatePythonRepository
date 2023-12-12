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


print("Your on vending machine")
def vending_machine(coins):
    total = 50
    if coins in [25, 10, 5]:
        total = total - coins
        print(f"You have {coins} inser coin")
vending_machine("coins: ")