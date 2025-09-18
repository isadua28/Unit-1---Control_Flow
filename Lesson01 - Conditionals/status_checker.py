# Student Information System - Starter Code

print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
gpa = float(input("Enter student GPA (0.0-4.0): "))

# Show student information
print()
print("STUDENT INFORMATION:")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print()

if name == "":
    print("Error: Name cannot be empty")
    
# TODO: Check if age is valid (between 16 and 100)
if age < 16 or age > 100:
    print("Error: Age must be a valid number ")
    
# TODO: Check if GPA is valid (between 0.0 and 4.0)
if gpa < 0.0 or gpa > 4.0:
    print("Error: GPA must be between 0.0-4.0")
print("")

# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)
if age >= 18 and gpa >= 2.0:
    print("ELIGIBLE for enrollment")
else:
    print("NOT ELLIGIBLE for enrollment")

# TODO: Check voting eligibility (age >= 18)
if 18 <= age <= 100:
    print("ELIGIBLE to vote")
else: 
    print("NOT ELIGIBLE to vote")
    
# TODO: Check honor roll status (gpa >= 3.5)
if 3.5 <= gpa <= 4.0:
    print("ON HONOR ROLL")
else: 
    print("NOT ON HONOR ROLL")