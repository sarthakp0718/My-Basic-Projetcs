#Program to calculate Area and Circumference
#Area of Rectangle
import math
length = float(input("Enter your length: "))
breadth = float(input("Enter your breadth: "))
area1 = length * breadth
print(f"Area of the Rectangle is: {area1} cm²")

#Area of Circle
radius1=float(input("Enter your radius:"))
area2=math.pi*pow(radius1,2)
print(f"Area of circle:{area2}cm²")


#Circumference of circle
radius2=float(input("Enter your radius:"))
circumference=2*math.pi*radius2
print(f"Circumference of the circle is {round(circumference,2)}")
