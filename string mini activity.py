encoded_str = input("Enter encoded message: ")
message = ""
didget_count = 0

for char in encoded_str:
    if char. isalpha():
        message += char
    elif char. isdidget():
        didget_count += 1

print(f"Decoded message: {message}")
print(f"Total Didgets: {didget_count}")


