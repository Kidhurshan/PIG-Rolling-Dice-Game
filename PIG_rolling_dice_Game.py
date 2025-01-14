import random


FinalScore = 40
StartingPlayerNumber = 1

#set the number of the player
playerCounts = int(input("Enter the number of players (2-4): "))
#set the player score
playerScoresList =[0 for _ in range(playerCounts)]
playerNumber = StartingPlayerNumber


def PrintPlayerIntro():
    print("")
    print(
        f"-------------------Player number {playerNumber} turns has just started!-----------------")  # set the player 1 to play
    print(f"Your total score is : {playerScoresList[playerNumber - 1]}")  # print the player 1 total score
    print("")




while(True):
    PrintPlayerIntro()
    while (True):
        userInput = input("Would you like to roll? (y/n): ").lower()    #ask to roll the dice
        if(userInput == "y"):
            randomDiceNumber = random.randint(1,6)          #display the random number
            if(randomDiceNumber != 1):                          #check whether random number is not 1
                playerScoresList[playerNumber-1] += randomDiceNumber             #add that into score of the player 1
                print(f"You rolled a : {randomDiceNumber}")
            else:
                playerScoresList[playerNumber-1] =0
                print(f"You rolled a 1! Turn done!!!")
                break

            print(f"Your total score is : {playerScoresList[playerNumber-1]}")
            if playerScoresList[playerNumber-1]> FinalScore:        #if the score >50
                print(f"Player number {playerNumber} is the winner with the score {playerScoresList[0]}")
                break
        else:
            break
    if playerScoresList[playerNumber - 1] > FinalScore:  # if the score >50
        break
    if playerNumber == playerCounts:
        playerNumber =1
    else:
        playerNumber +=1



