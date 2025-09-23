print("=== BMI Calculator ===")
height = float(input("Enter your height (in): "))
weight = float(input("Enter your weight (lbs): "))
print("")

print("=== BMI Health Report ===")
print("")

bmi = round((weight / (height**2)) * 703, 1)

print(f'Height: {height}"')
print(f"Weight: {weight} lbs")
print(f"BMI: {bmi}")
if height > 0.0 and weight > 0.0:
    category = ("Underweight" if bmi < 18.5 else 
                "Normal" if 18.5 <= bmi <= 25 else
                "Overweight" if 25 <= bmi < 30 else
                "Obese")
else: 
    print("Enter valid height or weight")
    
print(f"Category: {category}")
rec = "Gain / Maintain weight" if bmi <= 25 else "Lose weight"
health_risk = "Low" if bmi <= 25 else "Moderate / High"
print(f"Recommendation: {rec}")
print(f"Health Risk: {health_risk}")