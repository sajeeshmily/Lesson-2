
print("====================================")
print("      HOMEWORK COMPLETION TRACKER")
print("====================================")

homework = ["Mathematics", "Science", "English", "Computer"]

completed = []

while len(homework) > 0:

    print("\nPending Homework:", homework)

    task = homework[0]

    answer = input("\nHave you completed " + task + "? (yes/no): ").lower()

    if answer == "yes":
        print("Well done! " + task + " homework completed.")

        completed.append(task)
        homework.remove(task)

    elif answer == "no":
        print("Keep working! Complete your homework first.")

    else:
        print("Invalid input! Please enter yes or no.")

print("\n====================================")
print("       ALL HOMEWORK COMPLETED!")
print("====================================")

print("\nCompleted Homework:")

for task in completed:
    print("-", task)

print("\nTotal Tasks Completed:", len(completed))

print("\nGreat job! Keep up the good work!")
