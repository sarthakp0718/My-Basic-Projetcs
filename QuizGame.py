questions = ("1. What is the largest planet in our solar system?",
             "2. Which is the most abundant element in the universe?",
             "3. What element is the most commonly used to create nuclear energy?",
             "4. Who is credited with coming up with the theory of evolution?",
             "5. What is hydrogen oxide?")

options = (("A. Earth", "B. Jupiter", "C. Mars", "D. Uranus"),
           ("A. Hydrogen", "B. Oxygen", "C. Nitrogen", "D. Palladium"),
           ("A. Uranium", "B. Thorium", "C. Magnesium", "D. Gold"),
           ("A. Virat Kohli", "B. Albert Einstein", "C. Charles Darwin", "D. Nolan"),
           ("A. Methane", "B. Alcohol", "C. Glucose", "D. Water"))

answers = ("B", "A", "A", "C", "D")

guesses = []
score = 0

for question_num in range(len(questions)):
    print("___________________________________________")
    print(questions[question_num])

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A), (B), (C), (D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT ANSWER!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the right answer")

print("---------------------------------")
print("        RESULT         ")
print("----------------------------------")
print("Answers: ", end="")
print(" ".join(answers))

print("Your guesses: ", end="")
print(" ".join(guesses))

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")
