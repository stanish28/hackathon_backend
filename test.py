from random import *
print()
print("Welcome to IncNumber Game")
print()
print("LET'S  START")
j = "Yes"
i = 0
a = 0
while a <= 0:
 if j == "Yes" or j == "y" or j == "yes":
    while i <= 5:
     print("Game is on")
     p1 = int(input("Enter your number - "))
     print()
     comp = str(p1+(randint(0,100)))
     print("Computer's Number - " + comp)
     i+=1  
     print()
    print("Do you want to continue")
    j = input()   
 else:
    print()
    print("Game Over")
    break
     


###4no_of_players = int(input("Number of players - "))
#print(no_of_players)
#comp_play = input("Do you want computer to play?  ")
#print(comp_play)