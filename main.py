import random 
''' 
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1,1,0]) 
youstr = input("Enter you choice:")
youDict = { 
            "s":1,
            "w":-1,
            "g": 0
           }
reverseDict = {
    1: "Snake",
    -1:"Water",
    0: "Gun"
}
you = youDict[youstr]
print(f"You choose {reverseDict[you]} and \n Computer choose {reverseDict[computer]}")
'''
here if computer - you == 1 or-2 then you win else you loosse 
 so
 if(computer - you == 1 or computer -you == -2):
   print("you win!")
 else :
   print("you loose!") 
'''
if(computer == you):
    print("Its a draw!")
else :
    if(computer == -1 and you == 1): # computer -you == -2
        print("You Win!")

    elif(computer == -1 and you ==0): #computer -you == -1
        print("You Lose!")

    elif(computer == 1 and you == 0): # computer -you == 1
        print("You Win! ")

    elif(computer == 1 and you ==-1): # computer -you == 2
        print("You Lose!")

    elif(computer == 0 and you == -1): # computer -you == 1
        print("You Win!")

    elif(computer == 0 and you == 1): # computer -you == -1
        print("You Lose!")

    else :
        print("Something went Wrong!")
