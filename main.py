
import random   #   random is a Python module used to perform random operations

def play_game():
    #def is used to create a function, A function is a block of code that does a specific task

    print("Welcome to Color Guessing Game!")



    play_again = "yes"


    score = 0

    # Statistics
    total_games = 0
    correct_guesses = 0
    wrong_guesses = 0
    games_won = 0

    while play_again == "yes":
    #It repeats the game as long as the value of play_again is yes

        
        attempts = 5
        total_games = total_games + 1
        

        colors = ["red", "blue", "green", "yellow", "pink", "white", "grey", "purple", "black"]
        
        secret_color = random.choice(colors) #choice() is a function of the random module that randomly selects one item from a list

    
        print("The computer has selected a color!")

        print("Choose a color:")
        print(colors)

        while attempts > 0:

            print("Attempts remaining:", attempts)
            
            guess = get_guess()
 

            if guess not in colors:  #This condition checks whether the user's guessed color is not present in the colors list.
                print("Invalid color! Please choose a color from the list.")
                continue

    

            #if guess == secret_color:
            if check_guess(guess, secret_color): #new added after creating function   
                print("Correct! You guessed the color!")
                correct_guesses = correct_guesses + 1 #
                games_won = games_won + 1   
                #games_won = games_won + 1 is used to increase the value of gameswon by 1.


                #score = score + 10 # used before function 
                score = update_score(score) # used after function
                break
    
    




            else: #else is used when the if condition is false
                print("Wrong guess! Try again.") 
            
                wrong_guesses = wrong_guesses + 1
                attempts = attempts - 1
        #This statement decreases the value of attempts by 1 after a wrong guess
            if attempts == 0:
                print("No attempts left!")
                print("The correct color was:", secret_color)


        print("Your score is:", score)   


        play_again = input("Do you want to play again? (yes/no): ")


        if play_again == "yes":  

            print("Let's play again!")

        else:
            print("Thanks for playing!") 

            winning_percentage = (games_won / total_games) * 100


            print("\n--- Game Statistics ---")
            print("Total games played:", total_games)
            print("Correct guesses:", correct_guesses)
            print("Wrong guesses:", wrong_guesses)
            print("Final score:", score)
            print("Winning percentage:", winning_percentage)









def get_guess():  #get_guess() is a function created to take the users color guess as input
    #This function will handle the users guess input separately from the main game code
     guess = input("Enter your guess: ").lower()
     return guess

def check_guess(guess, secret_color):  #check_guess() is a function used to check whether the users guess matches the computers selected color
    if guess == secret_color:
        return True
    else:
        return False

def update_score(score):
    score = score + 10
    return score    

play_game()  