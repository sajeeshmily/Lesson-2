
print("===== DECIMAL TO BINARY CONVERSION =====")

num = int(input("Enter a decimal number: "))

original = num
binary = ""

if num < 0:
    print("Please enter a positive number.")

elif num == 0:
    binary = "0"

else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    print("Decimal Number:", original)
    print("Binary Number:", binary)

if original == 0:
    print("Decimal Number:", original)
    print("Binary Number:", binary)

print("Thank you!")
