age = int(input("Enter your age: "))
rating = input("Enter movie rating: ")
print(f"Age = {age}, Rating = {rating}")

if age:
    if rating == "G":
        print("APPROVED: You can watch this movie!")
    elif rating == "PG":
        if age < 6:
            print("DENIED: You must be 6+ to watch PG movies")
        elif age >= 6:
            print("APPROVED: You can watch this movie!")
    elif rating == "PG-13":
        if age < 13:
            print("WARNING: Not recommended for your age")
        elif age >= 13:
            print("APPROVED: You can watch this movie!")
    elif rating == "R":
        if age < 17:
            print("DENIED: Must be 17+ for R-rated movies")
        elif age >= 17:
            print("APPROVED: You can watch this movie!")
else:
    print("ERROR: Please enter your age")