password = input("Enter a password: ")

total_chars = len(password)
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_char_count = 0

print("")
print("PASSWORD ANALYSIS:")
print("=" * 20)
print(f"Password: '{password}'")

print("")
print("CHARACTER COUNTS: ")

for char in password: 
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    if 'a' <= char <= 'z':
        lowercase_count += 1
    if '0' <= char <= '9':
        digit_count += 1
    if '!' <= char <= '/': 
        special_char_count += 1

print(f"Length: {total_chars}")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_char_count}")
print("")

print("REQUIREMENTS CHECK:")
print("Length (8+ characters): PASSED") if total_chars >= 8 else print("Length (8+ characters): FAILED")
print("Uppercase letters: PASSED") if uppercase_count >= 1 else print("Uppercase letters: FAILED")
print("Lowercase letters: PASSED") if lowercase_count >= 1 else print("Lowercase letters: FAILED")
print("Digits: PASSED") if digit_count >= 1 else print("Digits: FAILED")
print("Special characters: PASSED") if special_char_count >= 1 else print("Special characters: FAILED")
print("")

print("SECURITY ISSUES: ")
for i in range(total_chars - 2):
    if password[i] == password[i+1] == password[i+2]:
        print(f"Repeated characters")
        break
    else:
        print("No repeated characters")
        break

for i in range(total_chars - 2):
    if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
        print(f"Contains sequence: {password[i:i+3]}")
    else: 
        print("No sequences")
        break
    
print("")
        
if total_chars and uppercase_count and lowercase_count and digit_count and special_char_count:
    print("FINAL RATING: STRONG")
else: 
    print("FINAL RATING: MEDIUM or WEAK")
