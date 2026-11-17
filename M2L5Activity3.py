
print("================================")
print("       NUMBER DIAMOND")
print("================================")

rows = int(input("Enter the number of rows: "))

# Upper half of the diamond
for i in range(1, rows + 1):

    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")

    # Print numbers
    for k in range(1, i + 1):
        print(k, end=" ")

    print()

# Lower half of the diamond
for i in range(rows - 1, 0, -1):

    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")

    # Print numbers
    for k in range(1, i + 1):
        print(k, end=" ")

    print()

print("\nPattern completed!")
