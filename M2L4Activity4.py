
print("===== MIDDLE DIGIT PRODUCT =====")

num = input("Enter a number: ")

length = len(num)

if not num.isdigit():
    print("Please enter a valid positive number.")

elif length % 2 == 1:
    mid = length // 2
    product = int(num[mid])
    print("Middle digit:", num[mid])
    print("Middle product:", product)

else:
    mid = length // 2
    digit1 = int(num[mid - 1])
    digit2 = int(num[mid])
    product = digit1 * digit2

    print("Middle digits:", digit1, "and", digit2)
    print("Middle product:", product)

print("Thank you!")
