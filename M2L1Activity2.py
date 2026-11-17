
print("===== ELECTRICITY BILL CALCULATOR =====")

name = input("Enter customer name: ")
units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid unit consumption!")

elif units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

elif units <= 300:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

else:
    bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

if units >= 0:
    print("\n----- ELECTRICITY BILL -----")
    print("Customer Name:", name)
    print("Units Consumed:", units)
    print("Total Bill: ₹", bill)

print("\nThank you!")
