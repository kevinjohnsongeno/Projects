import random

while True:
    print("WELCOME TO THE DICE ROLLING GAME!")
    ip=(input("Enter your choice whether you want to play the game or not?y/n").strip())
    if ip.upper()=='Y' :
        d1= random.randint(1, 6)
        d2= random.randint(1, 6)
        print(f"The dice are {d1} , {d2}")
    elif ip.upper()=='N':
        print("THANKS FOR PLAYING")
        break
    else:
        print("Invalid input")