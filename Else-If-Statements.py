score = int(input("Enter Score: "))
balls = int(input("Enter number of balls played: "))

if balls == 0:
    print("Balls faced cannot be zero.")
else:
    strike_rate = (score / balls) * 100
    print("Strike rate of the batsman is:", round(strike_rate, 2))
    if strike_rate > 150:
        print("Outstanding performance!")
    elif strike_rate > 100:
        print("Good performance.")
    elif strike_rate > 50:
        print("Average performance.")
    else:
        print("Needs improvement.")
