import random
computerWins = 0
computerLosses = 0
userWins = 0
userLosses = 0
ties = 0

def getComputerToChoose():
    computerChoices = ["Rock", "Paper", "Scissors"]
    word = random.choice(computerChoices)
    return word.upper()


def getUserInput(x):
    placeholder = x.upper()
    if placeholder == "ROCK" or placeholder == "PAPER" or placeholder == "SCISSORS":
        #print("working!")
        return placeholder
    else:
        print("Must Be a valid Input of exactly Rock, Paper or Scissors")
        placeholder = input("Enter Rock Paper or Scissors:")
        placeholder = placeholder.upper()
        return placeholder     

def playAgain():
    userInputContinue = input("Yes/No?:")
    userInputContinue = userInputContinue.upper()
    if userInputContinue == "YES":
        userInput = input("Enter Rock Paper or Scissors:")
        usersChosenWord = getUserInput(userInput)
        computersChosenWord = getComputerToChoose()
        primaryFunctionComparingWords(computersChosenWord, usersChosenWord)
    elif userInputContinue == "NO":
        print("Thanks for playing! If You want to Play Again just type Yes on the keyboard")
        playAgain()        
    else:
        print("That wasn't Yes or No")
        playAgain()
        
        
def scoreBoardFunction(placeholder):
    global computerWins
    global computerLosses
    global userWins
    global userLosses
    global ties  
    
    if placeholder == "CW":
        computerWins = computerWins + 1
        userLosses = userLosses + 1
        
    elif placeholder == "UW":

        userWins = userWins + 1
        computerLosses = computerLosses +1
        
    elif placeholder == "T":
        ties = ties + 1     

    print('''             ==========================================
            | Computer        Ties    Me               |
            | -------------   -----   -------------    |
            | Wins | Losses  -------  Wins | Losses    |    
            |''',"",computerWins, "     ", computerLosses, "      ",ties, "    ",userWins,"     ", userLosses, '''      |
             ==========================================''' )
        
    
        
        
def primaryFunctionComparingWords(computerPlaceholder, myPlaceholder):
    if computerPlaceholder == "ROCK" and myPlaceholder == "ROCK":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "Its a tie! Do you want to play Again?")
        scoreBoardFunction("T")
        playAgain()
        
    elif computerPlaceholder == "ROCK" and myPlaceholder == "SCISSORS":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "You lose! Want to play Again?")
        scoreBoardFunction("CW")
        playAgain()
        
    elif computerPlaceholder == "ROCK" and myPlaceholder == "PAPER":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "You Win! Want to play Again?")
        scoreBoardFunction("UW")
        playAgain()
        
    elif computerPlaceholder == "PAPER" and myPlaceholder == "SCISSORS":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "You Win! Want to play Again?")
        scoreBoardFunction("UW")
        playAgain()
        
    elif computerPlaceholder == "PAPER" and myPlaceholder == "PAPER":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "Its a tie! Do you want to play Again?")
        scoreBoardFunction("T")
        playAgain()
        
    elif computerPlaceholder == "PAPER" and myPlaceholder == "ROCK":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "You lose! Want to play Again?")
        scoreBoardFunction("CW")
        playAgain()
        
    elif computerPlaceholder == "SCISSORS" and myPlaceholder == "SCISSORS":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "Its a tie! Do you want to play Again?")
        scoreBoardFunction("T")
        playAgain()
        
    elif computerPlaceholder == "SCISSORS" and myPlaceholder == "PAPER":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "You lose! Want to play Again?")
        scoreBoardFunction("CW")
        playAgain()
        
    elif computerPlaceholder == "SCISSORS" and myPlaceholder == "ROCK":
        print("You chose", myPlaceholder, "and the computer chose", computerPlaceholder, "You Win! Want to play Again?")
        scoreBoardFunction("UW")
        playAgain()  

def main():
    opening = "| Welcome to my Rock, Paper, Scissors Game! |"
    print(len(opening) * "_", "\n")
    print(opening)
    print(len(opening) * "_", "\n")
    userInput = input("Enter Rock, Paper, or Scissors to start:")
    usersChosenWord = getUserInput(userInput)
    computersChosenWord = getComputerToChoose()
    primaryFunctionComparingWords(computersChosenWord, usersChosenWord)
    

main()
