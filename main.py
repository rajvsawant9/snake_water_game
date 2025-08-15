import random

'''snake = 1
water = -1
gun = 0
'''

computer = random.choice([1,-1,0]) # this inputn is random given b y the computer 
usermeans_you = input("enter your choice :")
youDict = {"s":1, "w":-1, "g":0}

you = youDict[usermeans_you] # this input is given is give by the user 

#BY now we have 2 variables or numbers : you and computer 

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
    
# now this program will not show the input of the computerr 
# i have designed now advance program for this

