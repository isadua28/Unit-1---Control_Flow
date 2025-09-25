# Three forms of range() function

#1 range(stop)
for i in range(5): #0, 1, 2, 3, 4
    print(i)
    
#2 range(start, stop)
for i in range(2, 8): #2, 3, 4, 5, 6, 7
    print(i)
    
#3 range(start, stop, step)
for i in range (2, 16, 4): #2, 6, 10, 14
    print(i)
    
# counting backwards
for i in range(10, 1, -2): #10, 8, 6, 4, 2
    print(i)
    
# Countdown Timer
# import time
# for second in range(10, -1, -1):
#     print(f"{second}-seconds")
#     time.sleep(1) # wait 1 second between numbers
# if second == 0:
#     print("BLAST OFF! 🚀")
    
# Multiplication Table
# Take user input for the number and print the table 
# If the user submitted 5
# 5x1 = 5
# 5x2 = 10

number = int(input("Enter a number (1-12): "))
if 1 <= number <= 12:
    for i in range (1, 13): 
        result = number * i
        print(f"{number} x {i:2d} = {result:3d}")
else: 
    print("Please enter a number between 1 and 12")
    
