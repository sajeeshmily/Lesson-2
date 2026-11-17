
print("================================")
print("   SUM OF WHOLE NUMBERS")
print("================================")

num = int(input("Enter the last number: "))

total = 0

for i in range(num + 1):
    total = total + i

print("Sum of whole numbers from 0 to", num, "is:", total)

print("Thank you!")
