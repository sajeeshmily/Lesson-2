
print("======================================")
print("          SHOP BILLING SYSTEM")
print("======================================")

customers = int(input("Enter number of customers: "))

all_bills = []

# Outer loop: Process each customer
for i in range(customers):

    print("\n--------------------------------------")
    print("Customer", i + 1)
    print("--------------------------------------")

    items = int(input("Enter number of items in basket: "))

    bill = []

    # Inner loop: Process each item
    for j in range(items):

        print("\nItem", j + 1)

        name = input("Enter item name: ")
        price = float(input("Enter item price: "))

        # Skip invalid prices
        if price <= 0:
            print("Invalid price! Item skipped.")
            continue

        quantity = int(input("Enter quantity: "))

        # Skip invalid quantities
        if quantity <= 0:
            print("Invalid quantity! Item skipped.")
            continue

        total = price * quantity

        bill.append([name, quantity, price, total])

        print("Item added successfully!")

    all_bills.append(bill)

# Final billing report
print("\n======================================")
print("          DAILY BILLING REPORT")
print("======================================")

grand_total = 0

# Nested for loop: Display each customer's bill
for i in range(len(all_bills)):

    print("\nCustomer", i + 1)
    print("--------------------------------------")

    customer_total = 0

    for item in all_bills[i]:

        print(item[0], "| Quantity:", item[1],
              "| Price:", item[2],
              "| Total:", item[3])

        customer_total = customer_total + item[3]

    print("Customer Bill: Rs.", customer_total)

    grand_total = grand_total + customer_total

print("\n======================================")
print("Total Shop Collection: Rs.", grand_total)
print("======================================")
print("Thank you for shopping!")
