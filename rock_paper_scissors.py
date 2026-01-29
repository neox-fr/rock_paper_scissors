import random

comp=["rock", "paper", "scissors"]
def get_choices(comp):
    player_choice=input("enter (rock, paper, scissors):")
    computer_choice = random.choice(comp)
    choices={"player":player_choice, "computer":computer_choice}
    return choices

def check_win(player, computer, comp):
    print("you chose " + player + ", computer chose " + computer)
    #print(f"you chose {player}, computer chose {computer}")
    if player not in comp:
        return "Not valid"
    elif player==computer:
        return "draw"
    elif player=="rock":
        if computer=="scissors":
            return "rock smashes scissors so u win"
        else:
            return "paper gets rock so u lose"
        
    elif player=="paper":
        if computer=="scissors":
            return "scissors cuts paper so u lose"
        else:
            return "paper gets rock so u lose"
        
    elif player=="scissors":
        if computer=="paper":
            return "scissors cuts paper so u win"
        else:
            return " rock destroy scissors so u lose"

choices = get_choices(comp)
result = check_win(choices["player"], choices["computer"], comp)

print(result)
