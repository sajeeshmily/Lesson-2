
print("====================================")
print("          LOOP ART DESIGNER")
print("====================================")

print("\nChoose a pattern:")
print("1. Right-Angled Triangle")
print("2. Floyd's Triangle")
print("3. Number Diamond")
print("4. Star Pyramid")

choice = int(input("\nEnter your choice (1-4): "))

rows = int(input("Enter the number of rows: "))

if choice == 1:

    print("\nRight-Angled Triangle:\n")

    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

elif choice == 2:

    print("\nFloyd's Triangle:\n")

    num = 1

    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num = num + 1
        print()

elif choice == 3:

    print("\nNumber Diamond:\n")

    # Upper half
    for i in range(1, rows + 1):

        for j in range(rows - i):
            print(" ", end=" ")

        for k in range(1, i + 1):
            print(k, end=" ")

        print()

    # Lower half
    for i in range(rows - 1, 0, -1):

        for j in range(rows - i):
            print(" ", end=" ")

        for k in range(1, i + 1):
            print(k, end=" ")

        print()

elif choice == 4:

    print("\nStar Pyramid:\n")

    for i in range(1, rows + 1):

        for j in range(rows - i):
            print(" ", end=" ")

        for k in range(2 * i - 1):
            print("*", end=" ")

        print()

else:
    print("\nInvalid choice! Please select 1 to 4.")

print("\n====================================")
print("       THANK YOU FOR USING")
print("          LOOP ART DESIGNER")
print("====================================")
