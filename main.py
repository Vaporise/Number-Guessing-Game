import random

def main():

    loop = True #Initialised game loop
    
    print("What is the minimum number you would like to guess?")
    a = int(input())
    print("What is the maximum number you would like to guess?")
    b = int(input())

    num_of_guesses = 0
    high_score = 0

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
                num_of_guesses += 1
                print(f"You guessed {num_of_guesses} times")
                print("Do you want to play again?")
                answer = input().lower() #accept the answer regardless of case. Converted to lower case.
                if answer == "y":
                    if num_of_guesses < high_score: #check the high_score has been beaten.
                        high_score = num_of_guesses # if beaten then set the new high score.
                        print(f"You set a new highscore of {high_score}")
                    loop = True #Keeps the loop going if choosing to play more.
                else:    
                    loop = False #Ends the loop
                    exit #Exits the program.

            elif intguess > random_number:
                print("Too high!")
                num_of_guesses += 1
            elif intguess < random_number:
                print("Too low!")
                num_of_guesses += 1
            
if __name__ == "__main__":
    main()