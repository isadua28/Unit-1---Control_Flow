# syntax: 
'''
initialize variable
while condition (test variable): 
    code block
    increment/decrement
'''

# num = 5
# while num > 0:
#     print(num)
#     num -= 1
# print("Blastoff!")

# num = 1
# total = 0

# while num <= 10:
#     total += num # (total = total + num)
#     num += 1
# print(f"The sum of numbers 1-10: {total}")

# num = 1

# while num <= 10:
#     total += num
#     if num < 10:
#         print(num, end="+")
#     else:
#         print(num, end="=")
#     num += 1
# print(total)
# print()

# Sum of digits
# Take a user input as int, and sum the digits of it

# number = input("Enter a number: ") #1234
# sum = 0
# for char in number:
#     print(f"{char} {type(char)}")
#     sum += int(char)
# print(f"Tota {sum}")

# i = 0
# while i < len(number):
#     sum += int(number[i])
#     i += 1
# print(f"Total: {sum}")

# Algorithm - count digits (as ints)
# n = int(input("Enter a number: "))
# number = n
# count = 0
# while number > 0:
#     # Get the last digit
#     digit = number % 10
#     count += digit # Add to sum
#     number = number // 10 # Remove the last digit
# print(f"The sum of digits {n}: {sum}")

# Algorithm - count digits (as ints)
number = 54321
n = number
count = 0
while number > 0:
    count += 1
    number = number // 10
print(f"The number of digits {n}: {count}")