#USERNAME INPUT
#1.It should not contain any spaces.
#2.It should only contain alpahbets.
#3.It should contain only 12 digits.

user_name=input("Enter your username:").upper()

if len(user_name)>12:
    print("You're username cannot be more than 12 characters")
elif not user_name.isalpha():
    print("Your username can only contain alphabets")
elif not user_name.find(" ") ==-1:
    print("You're username cannot contain spaces")
else :
    print(f"Welcome {user_name}")