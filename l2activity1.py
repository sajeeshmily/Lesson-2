
print("================================")
print("     WELCOME TO VEHICLE WORLD")
print("================================")

print("\nChoose your vehicle:")
print("1. Bike")
print("2. Car")

choice = input("\nEnter your choice (Bike/Car): ").lower()

if choice == "bike":
    print("\nYou selected: Bike")
    print("\nChoose a bike model:")
    print("1. Royal Enfield")
    print("2. KTM")

    model = input("Enter model name: ").lower()

    if model == "royal enfield":
        print("\nVehicle Name: Royal Enfield")
        print("Top Speed: 120 km/h")
        print("Best Use: Long rides and touring")

    else:
        if model == "ktm":
            print("\nVehicle Name: KTM")
            print("Top Speed: 140 km/h")
            print("Best Use: Sports riding and adventure")

        else:
            print("Invalid bike model!")

elif choice == "car":
    print("\nYou selected: Car")
    print("\nChoose a car model:")
    print("1. Hyundai Creta")
    print("2. Maruti Swift")

    model = input("Enter model name: ").lower()

    if model == "hyundai creta":
        print("\nVehicle Name: Hyundai Creta")
        print("Seats: 5")
        print("Best Use: Family trips and city driving")

    else:
        if model == "maruti swift":
            print("\nVehicle Name: Maruti Swift")
            print("Seats: 5")
            print("Best Use: Daily commuting and city driving")

        else:
            print("Invalid car model!")

else:
    print("\nInvalid vehicle choice!")

print("\nThank you for visiting Vehicle World!")
print("GOODBYE!")
