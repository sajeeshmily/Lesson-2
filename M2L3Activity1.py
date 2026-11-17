print("===== SUM OF NATURAL NUMBERS =====")

n = int(input("Enter the number: "))

total = 0

if n <= 0:
    print("Please enter a positive number.")

else:
    for i in range(1, n + 1):
        total = total + i

    print("Sum of first", n, "natural numbers is:", total)

print("Thank you!")