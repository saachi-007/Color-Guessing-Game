
import random   #   random is a Python module used to perform random operations.

def play_game():
    #def is used to create a function. A function is a block of code that does a specific task.

    print("Welcome to Color Guessing Game!")

#import random can also be written inside a function, but keeping imports at the top of the file is generally cleaner and easier to manage.

    play_again = "yes"
# play_again = "yes": It stores the initial value "yes" in the play_again variable so that the game can start and repeat using a while loop.

    score = 0

    while play_again == "yes":
    #It repeats the game as long as the value of play_again is "yes".

        
        attempts = 3

        colors = ["red", "blue", "green", "yellow","pink", "white"]

        secret_color = random.choice(colors) #choice() is a function of the random module that randomly selects one item from a list

    
        print("The computer has selected a color!")

        print("Choose a color:")
        print(colors)

        while attempts > 0:

            print("Attempts remaining:", attempts)
            
            guess = get_guess()

            #guess = input("Enter your guess: ").lower()   #.lower() converts all letters in a string to lowercase.
# input() → A function used to take input from the user
# guess → A variable used to store the user's guessed color

            if guess not in colors:  #This condition checks whether the user's guessed color is not present in the colors list.
                print("Invalid color! Please choose a color from the list.")
                continue

    

            #if guess == secret_color:
            if check_guess(guess, secret_color): #new added after creating function   
                print("Correct! You guessed the color!")
                #score = score + 1 # used before function 
                score = update_score(score) # used after function
                break
    # if =is used to check whether a condition is true
    #== is operator  used to check whether two values are equal

            else: #else is used when the if condition is false
                print("Wrong guess! Try again.") 
            #print("The correct color was:", secret_color)
            attempts = attempts - 1
        #This statement decreases the value of attempts by 1 after a wrong guess.
            if attempts == 0:
                print("No attempts left!")
                print("The correct color was:", secret_color)



        print("Your score is:", score)   
# We want to give the player an option to play the game again  then 

        play_again = input("Do you want to play again? (yes/no): ")
# Ask the player whether they want to play again and store their answer in the play_again variable

        if play_again == "yes":  #We check the player's answer to see whether they want to play again

            print("Let's play again!")

        else:
            print("Thanks for playing!")    


def get_guess():  #get_guess() is a function created to take the user's color guess as input.
    #This function will handle the user's guess input separately from the main game code.
     guess = input("Enter your guess: ").lower()
     return guess

def check_guess(guess, secret_color):  #check_guess() is a function used to check whether the user's guess matches the computer's selected color.
    if guess == secret_color:
        return True
    else:
        return False

def update_score(score):
    score = score + 1
    return score    

play_game()  