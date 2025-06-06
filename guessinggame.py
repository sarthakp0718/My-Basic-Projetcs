secret_word="Virat"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False
while guess !=secret_word and not(out_of_guesses):
  if guess_count< guess_limit:
    guess_count += 1
    guess=input("Enter your word:")
  else:
     out_of_guesses=True

if out_of_guesses:
    print("Out of guesses,YOU LOSE")
else:
    print("You win")
  