#Python Number guessing Game
import random
low=0
high=20
answer=random.randint(low,high)
guesses=0
is_running=True
print("Python Number Guess Game!")
print(f"Choose a Number between {low} and {high} :")
while is_running:
    guess=input("Guess a Number:")

    if guess.isdigit():
      guess=int(guess)
      guesses+=1
      if guess<low or guess>high:
       print("Number is out of the range")
      pass
    else:
      print("Invalid Guess")
      print(f"Please Select a Number between {low} and {high} :")