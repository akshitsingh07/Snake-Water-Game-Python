import random
from typing import DefaultDict


def gameWin(comp, you):
    if you == comp:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == 'g':
            return True
    elif you == 'w':
        if comp == 'g':
            return True
        elif comp == 's':
            return False
    elif you == 'g':
        if comp == 'w':
            return False
        elif comp == 's':
            return True

    # if you != comp.string():
    #     print("Invalid Choice")
print("Computer Turn: Snake(s), Water(w) or Gun(g)?: ")
randNo = random.randint(1, 3)

# print(randNo)
if randNo == 1:
    comp = "s"
if randNo == 2:
    comp = "w"
if randNo == 3:
    comp = "g"
you = input("Your Turn: Snake(s) Water(w) or Gun(g): ")

a = gameWin(comp, you)

print(f"The Computer Choose: {comp}")
print(f"And You Choose: {you}")

if a == None:
    print("The Game is Tie!")
elif a: #For true Value comes from the loop
    print("You Win!")
else:  # For true Value comes from the loop
    print("You Loose!")
