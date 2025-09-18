# # ========================================
# # ACCELERATED PYTHON UNIT 2 - LESSON 1
# # Conditionals: JavaScript to Python
# # ========================================

# # ========================================
# # SECTION 1: QUICK TRANSLATION CHALLENGE
# # ========================================
# print("===Grade Classification===")
# score = 87
# if score >= 90:
#     print("A grade")
# elif score >= 80:
#     print("B grade")
# elif score >=70: 
#     print("D grade")
# else:
#     print("F grade")
# # ========================================
# # SECTION 2: AGE CATEGORY CLASSIFIER
# # ========================================
# age_input = int(input("Enter your age: "))
# if age_input:
#     if 0 <= age_input <= 12:
#         print("You are a child")
#     elif 13 <= age_input <= 19:
#         print("You are a teenager")
#     elif 20 <= age_input <= 64: 
#         print("You are an adult")
#     elif age_input >= 65:
#         print("You are a senior")
#     else:
#         print("Please enter a valid age")
# else: 
#     print("Please enter a valid age")
# ========================================
# SECTION 3: STUDENT STATUS CHECKER
# ========================================

# age = 17
# gpa = 3.8
# has_license = True

# can_drive = age >= 16 and has_license
# honor_roll = gpa >= 3.5
# eligible = can_drive and honor_roll and age >= 17

# print(f"Can drive: {can_drive}")
# print(f"Honor roll: {honor_roll}")
# print(f"Eligible: {eligible}")

# if eligible: 
#     print("Scholarship candidate")

# ========================================
# SECTION 4: GRADE VALIDATOR CHALLENGE
# ========================================


# ========================================
# SECTION 5: WEATHER DECISION SYSTEM
# ========================================
