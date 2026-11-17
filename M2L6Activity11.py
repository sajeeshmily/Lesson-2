
print("===== POLYGON PATTERN =====")

sides = int(input("Enter the number of sides (3 to 10): "))

if sides < 3 or sides > 10:
    print("Please enter sides between 3 and 10.")

else:
    for i in range(sides):
        for j in range(sides):
            print("*", end=" ")
        print()

print("Thank you!")
