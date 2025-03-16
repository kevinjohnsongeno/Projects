import random
emo={"r":"🪨","p":"📃","s":"✂️"}
c=["r","p","s"]
def get_choice():
    while True:
        uc=input("ROCK,PAPER,SCISSORS(r,p,s)").lower()
        if uc in c:
            return uc
        else:
            print("Invalid choice")
           

def display_choice(uc,cc):
    print(f"Computer chose:{emo[cc]}")
    print(f"You chose:{emo[uc]}")
def final_step(uc,cc):
    if cc==uc:
        return "TIE" 
    elif (cc=='r' and uc=='p') or (cc=='s' and uc=='r') or (cc=='p' and uc=='s'):
        return "You won" 
    else:
        return "Computer won" 
def game():
    while True:
            uc=get_choice()
            cc= random.choice(c)
            display_choice(uc,cc)
            print(final_step(uc,cc))
            
            con=input("Do you want to continue(y/n)").lower()
            if con=="n":
                break
        
game()
        