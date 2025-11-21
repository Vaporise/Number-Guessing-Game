import random

def main():

    loop = True #Initialised game loop
    
    print("What is the minimum number you would like to guess?")
    a = int(input())
    print("What is the maximum number you would like to guess?")
    b = int(input())

    random_number = random.randint(a, b) #Random Number to guess

    while loop == True: #Game loop
        print(f"Guess the number between {a} and {b}")
        guess = input() #User entered guess
        intguess = int(guess)

        if intguess > b or intguess < a: #Check to see if number entered is outside of number range.
            print("Your guess is outside the number limits")
            intguess = input()
        else:
            if intguess == random_number:
                print("Congratulations! You guessed the number")
                loop = False
                exit

            elif intguess > random_number:
                print("Too high!")
            elif intguess < random_number:
                print("Too low!")
            
if __name__ == "__main__":
    main()