#kindly play with input as [s,w,g]

import random

'''snake = 1
water = -1
gun = 0
'''

computer = random.choice([1,-1,0]) # this inputn is random given b y the computer 
usermeans_you = input("enter your choice :")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"} # this is used to show what will the computer gives the input

you = youDict[usermeans_you] # this input is given is give by the user 

#BY now we have 2 variables or numbers : you and computer 

print(f"your choice : {reverseDict[you]}\ncomputer choice : {reverseDict[computer]}") #this is done for advanced

if (computer == you):
    print("its a draw") # this is the base statement if both the input value becomes same 

else:
    if(computer ==1 and you == -1):
        print("you loss")
    
    elif(computer ==1 and you == 0):
        print("you win")
    
    elif(computer ==-1 and you == 1):
        print("you win")
    
    elif(computer ==-1 and you == 0):
        print("you loss")
    
    elif(computer ==0 and you == 1):
        print("you loss")
    
    elif(computer ==0 and you == -1):
        print("you win")

    else :
        print("something went wrong!")
    
