# Converting temperature into different units
unit = input("Is this temperature in Celsius (C), Fahrenheit (F), or Kelvin (K)? : ").upper()
temp = float(input("Enter the Temperature: "))

if unit == "C":
    F = round((9 * temp) / 5 + 32, 1)
    K = 273.15 + temp
    print(f"Temperature in Fahrenheit is {F} °F")
    print(f"Temperature in Kelvin is {K} K")
elif unit == "F":
    C = round((temp - 32) * 5/9, 1)
    K = round((temp - 32) * 5/9 + 273.15, 1)
    print(f"Temperature in Celsius is {C} °C")
    print(f"Temperature in Kelvin is {K} K")
elif unit == "K":
    C = round(temp - 273.15, 1)
    F = round((temp - 273.15) * 9/5 + 32, 1)
    print(f"Temperature in Celsius is {C} °C")
    print(f"Temperature in Fahrenheit is {F} °F")
else:
    print("Invalid input! Please enter C, F, or K.")

