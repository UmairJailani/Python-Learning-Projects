unit = input("Is you height in (m)eters or (c)m? ").lower()
height = float(input("What is your height in meters? "))
weight = float(input("what is your weight in kg? "))

if unit == "c":
    height = height / 100

bmi = weight / (height ** 2)

round(bmi , 2)
print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
elif bmi < 30:
    print("You are Class I obese")
elif bmi < 39:
    print("You are Class II obese")
else:
    print("You are Class III obese")
