import random
option=("Rock","Paper","Scissors")
player=None
computer=random.choice(option)

player=input("Enter a choice(Rock,Paper,Scissors)")
print(f"Player:{player}")
print(f"Computer:{computer}")