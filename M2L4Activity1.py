
print("====================================")
print("          DAILY ATM SESSION")
print("====================================")

atm_balance = 100000

notes_500 = 100
notes_200 = 100
notes_100 = 200

customers = int(input("\nEnter number of customers today: "))

customer_count = 1

while customer_count <= customers:

    print("\n------------------------------------")
    print("Customer", customer_count)
    print("------------------------------------")

    pin = input("Enter your ATM PIN: ")

    if pin == "1234":

        balance = 10000
        transaction = "yes"

        while transaction == "yes":

            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your balance is Rs.", balance)

            elif choice == 2:
                amount = int(input("Enter deposit amount: "))
                balance = balance + amount
                atm_balance = atm_balance + amount
                print("Amount deposited successfully!")

            elif choice == 3:
                amount = int(input("Enter withdrawal amount: "))

                if amount <= balance and amount <= atm_balance:
                    balance = balance - amount
                    atm_balance = atm_balance - amount

                    print("Please collect your cash.")
                    
                    if amount >= 500:
                        n500 = amount // 500
                        amount = amount % 500
                        notes_500 = notes_500 - n500

                    if amount >= 200:
                        n200 = amount // 200
                        amount = amount % 200
                        notes_200 = notes_200 - n200

                    if amount >= 100:
                        n100 = amount // 100
                        amount = amount % 100
                        notes_100 = notes_100 - n100

                else:
                    print("Insufficient balance!")

            else:
                print("Invalid choice!")

            transaction = input(
                "\nDo you want another transaction? (yes/no): "
            ).lower()

    else:
        print("Incorrect PIN! Customer session ended.")

    customer_count = customer_count + 1

print("\n====================================")
print("          DAILY ATM REPORT")
print("====================================")

print("Total Customers Served:", customers)
print("Remaining ATM Balance: Rs.", atm_balance)

print("\nRemaining Currency Notes:")
print("Rs. 500 Notes:", notes_500)
print("Rs. 200 Notes:", notes_200)
print("Rs. 100 Notes:", notes_100)

print("\nATM Closed for Today!")
print("Thank you!")
