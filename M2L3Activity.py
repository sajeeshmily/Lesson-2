
print("====================================")
print("       CHORE CHECKLIST COUNTDOWN")
print("====================================")

chores = ["Make the bed", "Clean the room",
          "Wash the dishes", "Water the plants"]

completed = []

while len(chores) > 0:
    print("\nRemaining Chores:", chores)

    chore = chores[0]

    answer = input("\nHave you completed " + chore + "? (yes/no): ").lower()

    if answer == "yes":
        print("Great job! " + chore + " completed.")
        completed.append(chore)
        chores.remove(chore)

    else:
        print("No problem! Complete it and try again.")

print("\n====================================")
print("       ALL CHORES COMPLETED!")
print("====================================")

print("\nYour Completed Chores:")

for chore in completed:
    print("-", chore)

print("\nTotal Chores Completed:", len(completed))
print("Well done! Have a great day!")
