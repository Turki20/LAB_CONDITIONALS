
wieght:int = int(input("Enter your wieght (Kg): "))
height:int = int(input("Enter your height (cm): "))

# w(kg) / h(m)^2
bmi = wieght / (height / 100)**2
print(f"your BMI is: {round(bmi, 2)}")

if bmi > 30:  # > 30
    print("Obesity")
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi > 25 and bmi < 29.9: # 25 - 29.9
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi > 18.5 and bmi < 24.9: # 18.5 - 24.9
    print("You are fit & healthy.")
elif bmi < 18.5: # < 18.5
    print("You are underweight. Watch your health.")