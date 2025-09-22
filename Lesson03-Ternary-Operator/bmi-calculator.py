height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))
bmi = (weight / (height**2)) * 703

if height and weight:
    category = ("Underweight" if bmi < 18.5 else 
                "Normal" if 18.5 <= bmi <= 25 else
                "Overweight" if 25 <= bmi < 30 else
                "Obese")
else: 
    print("Enter valid height or weight")
    
print(f"You are {category}")