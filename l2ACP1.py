
print("====================================")
print("      HOLIDAY ACTIVITY PLANNER")
print("====================================")

print("\nWhat type of holiday do you prefer?")
print("1. Beach Holiday")
print("2. Mountain Holiday")
print("3. City Holiday")

choice = input("\nEnter your choice: ").lower()

if choice == "beach holiday":
    print("\nGreat! You chose a Beach Holiday.")
    print("\nWhat would you like to do?")
    print("1. Water Sports")
    print("2. Relax on the Beach")

    activity = input("Enter your activity: ").lower()

    if activity == "water sports":
        print("\nYour Holiday Plan:")
        print("Enjoy swimming, surfing and jet skiing!")
        print("Best time: Morning")

    else:
        if activity == "relax on the beach":
            print("\nYour Holiday Plan:")
            print("Enjoy sunbathing, reading and watching sunsets!")
            print("Best time: Evening")
        else:
            print("Invalid activity choice!")

elif choice == "mountain holiday":
    print("\nWonderful! You chose a Mountain Holiday.")
    print("\nWhat would you like to do?")
    print("1. Trekking")
    print("2. Camping")

    activity = input("Enter your activity: ").lower()

    if activity == "trekking":
        print("\nYour Holiday Plan:")
        print("Explore mountain trails and enjoy beautiful views!")
        print("Best time: Early Morning")

    else:
        if activity == "camping":
            print("\nYour Holiday Plan:")
            print("Enjoy campfires, stargazing and nature!")
            print("Best time: Night")
        else:
            print("Invalid activity choice!")

elif choice == "city holiday":
    print("\nWelcome to your City Holiday!")
    print("\nWhat would you like to do?")
    print("1. Shopping")
    print("2. Sightseeing")

    activity = input("Enter your activity: ").lower()

    if activity == "shopping":
        print("\nYour Holiday Plan:")
        print("Explore shopping malls and local markets!")
        print("Best time: Afternoon")

    else:
        if activity == "sightseeing":
            print("\nYour Holiday Plan:")
            print("Visit famous landmarks, museums and monuments!")
            print("Best time: Morning")
        else:
            print("Invalid activity choice!")

else:
    print("\nInvalid holiday choice!")

print("\nThank you for using Holiday Activity Planner!")
print("Have a wonderful holiday! Goodbye!")
