import random
while(1):
    user = int(input("Enter number between 1-6 "))
    comp = random.randrange(1, 6)
    if(user > comp):
        print("You Won")
        break
    elif(comp > user):
        print("You Lost")
        break
    else:
        print("Roll Again")
        pass
