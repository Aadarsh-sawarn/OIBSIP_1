# Making BMI Calculator

print("BMI CALCULATOR ")

# Getting input from user
weight = float(input("Please enter your weight (kg) (eg:45): "))
height = float(input("Please enter your height (m) (eg:1.6):"))

# Formula for calculating BMI
BMI = weight/(height*height)

# Conditions for different values of  BMI
if BMI <= 18.5:
    print("You are underweight! Your BMI is: ",BMI)
elif BMI >18.5 and BMI <= 24.99:
    print("SMILE :) !! You are normal and healthy. Your BMI is: " ,BMI)
elif BMI >= 25 and BMI <=29.9:
    print("You are overweight!! Your BMI is: " ,BMI) 
elif BMI >= 30.0:
    print("OBESE , Please have a diet and do Exercise to be healthy.Your BMI is: " ,BMI)
else:
    print("THANK YOU")              