
def define_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result *= base_num #or result=result*base_num ....# Multiplication shortcut
    return result

# Taking input correctly
base_num = int(input("Enter the base number: "))
power_num = int(input("Enter the power number: "))

# Calling function and printing result
print(base_num, "raised to the power of", power_num, "is:", define_to_power(base_num, power_num))

   