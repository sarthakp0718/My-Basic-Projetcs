#Python Calculator
operator=input("Enter an Operator(+,-,*,/):")
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))

if operator == "+" :
   print("Addition of the given numbers is ",num1+num2)
elif operator == "-" :
   print("Subtraction of the given numbers is ",num1-num2)
elif operator == "*" :
   print("Addition of the given numbers is ",num1*num2)
elif operator ==  "/":
   print("Addition of the given numbers is ",num1/num2)
else :
   print(f"{operator}is not valid operator")