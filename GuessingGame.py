import random as rd     #Import random library to generate random int numbers
print(" Welcome to number guessing game :) (Please, press r bu restart the game..) ")     #Simple title for game
number=rd.randint(0,101)   # Generate random number to predict
prediction=0 
while True:
    guess=float(input(" Please, guess a number between 0 and 100: "))  # User's prediction
    if guess>number: #
        print(" Please, input smaller number...") 
        prediction+=1
    elif guess<number:
        print(" Please, input bigger number...")
        prediction+=1
    else:
        prediction+=1
        print(" Congratulations !!! You find the number correctly in "+str(prediction)+" prediction ")
        
        key=input()
        if key=="r":
            prediction=0
            number=rd.randint(0,101)   # Generate random number again
            continue
            