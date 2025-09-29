text = input("Enter a text: ")
# initialize counters
total_chars = len(text)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

# Track first and last character: 
first_letter = None
last_letter = None

print(f"Analyzing: '{text}")
print("=" * 40)

# Process each character
for char in text:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count += 1
        if first_letter is None:
            first_letter = char
        last_letter = char # Keep updating (last one)
    # Count uppercase
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    # Count lowercase
    if 'a' <= char <= 'z':
        lowercase_count += 1
    # Count digit
    if '0' <= char <= '9':
        digit_count += 1

# Displaying the results
print(f"Total Characters: {total_chars}")
print(f"Letter count: {letter_count}")
print(f"Digit Count: {digit_count}")
print(f"Uppercase Count: {uppercase_count}")
print(f"Lowercase Count: {lowercase_count}")
print(f"First Letter: {first_letter}")
print(f"Last Letter: {last_letter}")

