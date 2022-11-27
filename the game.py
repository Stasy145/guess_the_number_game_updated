
import random
print("Hello! Welcome to the game! Can you guess the number?")

def guess_the_number_game():
    y = 1
    x = 15
    computer_choice = random.randint(y, x)
    user_guess = 0
    while user_guess != computer_choice:
        try:
            user_guess = int(input(f"Enter the number between {y} and {x}:   "))
        except:
            user_guess = -1
            if user_guess != int(): # works in case a user prints something different but a number
                print("Have you been to school?. Try a real number: ")
                break

        if user_guess > computer_choice:
            print("Sorry, your number is too high!")
            if user_guess < x:
                x = user_guess
            if user_guess > x:
                print("And it's out of range!")

        elif user_guess < computer_choice:
            print("Sorry, your number is too low!")
            if user_guess > y:
                y = user_guess
            if user_guess < y:
                print("And it's out of range!")

    print(f"Congrats! You guessed the number {computer_choice} correctly!")

guess_the_number_game()
