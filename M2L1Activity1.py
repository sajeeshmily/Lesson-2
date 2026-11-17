
print("===== EXAM ELIGIBILITY CHECKER =====")

name = input("Enter student name: ")
attendance = float(input("Enter attendance percentage: "))

if attendance < 0 or attendance > 100:
    print("Invalid attendance percentage!")

elif attendance >= 75:
    print("\nStudent Name:", name)
    print("Attendance:", attendance, "%")
    print("Status: Eligible for Examination")

else:
    print("\nStudent Name:", name)
    print("Attendance:", attendance, "%")
    print("Status: Not Eligible for Examination")

print("\nThank you!")
