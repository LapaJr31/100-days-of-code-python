mass = float(input("Hello! Input your mass in kg. "))
height = float(input("Enter your height in meters. "))

bmi = round(mass / height**2, 1)

print(f"Your bmi is {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5 > 24.9:
    print("You have normal weight")
elif bmi > 25 > 29.9:
    print("You are overweight")
elif bmi > 30 > 34.9:
    print("You are obese")
elif bmi > 35:
    print("You are extremely obese")
else:
    print("error")

