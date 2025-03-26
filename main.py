print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Start game by asking first question.
first = str(input("Left or right? ")).lower()
if first == 'left'.lower():
# If answer to first question is 'left', continue to second question.
    second = str(input("Swim or wait? ")).lower()
    
# If answer to first question is 'right', game over.
else:
    print("Fall into a hole. Game over.")
    
# If answer to second question is 'wait', continue to third question.
if second == 'wait':
    third = str(input("Which door? (red, yellow, or blue): ")).lower()
    
# If answer to second question is 'swim', game over.
else:
    print("Attacked by trout. Game over.")
    
# If answer to third question is 'red', game over.
if third == 'red':
    print("Burned by fire. Game over.")
    
# If answer to third question is 'blue', game over.
elif third == 'blue':
    print("Eaten by beasts. Game over.")
    
# If answer to third question is 'yellow', prints "You Win!".
elif third == 'yellow':
    print("You Win!")
# If answer to third question is anything else, game over.
else:
    print("Game Over.")
