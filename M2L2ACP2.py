
print("================================")
print("       POWER CALCULATOR")
print("================================")

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1

for i in range(exponent):
    result = result * base

print("\nBase:", base)
print("Exponent:", exponent)
print("Result:", result)

print("\nThank you for using Power Calculator!")
