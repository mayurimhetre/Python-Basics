### taking height in cm and  weight in kg from user

height = float(input("enter your height:"))
weight = float(input("Enter your Weight:"))


def bmi_calculator(height,weight):
    BMI = weight / (height/100)**2
    if BMI <= 18.4:
        print("You are underweight.")
    elif BMI <= 24.9:
        print("You are healthy.")
    elif BMI <= 29.9:
        print("You are over weight.")
    elif BMI <= 34.9:
        print("You are severely over weight.")
    elif BMI <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")
        
bmi_calculator(height,weight)
