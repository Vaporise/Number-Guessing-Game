import random

def main():

    loop = True #Initialised game loop
    random_number = random.randint(1, 100) #Random Number to guess

    while loop == True: #Game loop
        print("Guess the number between 1 and 100")
        guess = input() #User entered guess

        if guess > 100 or guess < 1: #Check to see if number entered is outside of number range.
            print("Your guess is outside the number limits")
            guess = input()
        else:
            if guess == random_number:
                print("Congratulations! You guessed the number")
                loop = False
                exit

            elif guess > random_number:
                print("Too high!")
            elif guess < random_number:
                print("Too low!")
            
if __name__ == "__main__":
    main()