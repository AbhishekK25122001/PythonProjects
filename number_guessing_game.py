import random

#Generate a random number
def generate_number():
    return random.randint(1,100)

#Get the user's guess
def get_users_guess():
    try:
        return int(input("Enter yoour guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None

#Check the user's guess
def check_guess(guess,number):
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too High!"
    else:
        return "Correct!"

#Main Game function
def play_game():
    number=generate_number()
    attempts=0
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")

    while True:
        guess=get_users_guess()
        if guess is None:
            continue
        attempts += 1
        result=check_guess(guess,number)
        print(result)

        if result=="correct!":
            print(f"you guessed the number in {attempts} attempts!")
            break

#Start the game
if __name__=="__main__":
    play_game()