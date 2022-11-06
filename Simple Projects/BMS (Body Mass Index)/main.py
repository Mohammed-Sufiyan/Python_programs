# This project is about Body Mass Index also known as BMI is usually used to see a person is underweight, healty, overweight
# The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters,
# then dividing the answer again by their height.

height = float(input("Enter your height in centimeter:- "))
weight = float(input("Enter your weight in kg:- "))
height = height / 100
BMI = weight / (height * height)
print("You Body Mass Index is :", BMI)
if BMI > 0:
    if BMI <= 16:
        print("You are severely underweight")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 25:
        print("You are Healty")
    elif BMI <= 30:
        print("You are overweight")
    else:
        print("You are severely overweight")
else:
    print("Enter valid details")
