
print("===== ARMSTRONG NUMBER CHECKER =====")

num = int(input("Enter a number: "))

original = num
temp = num
digits = len(str(num))

total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == original and original >= 0:
    print(original, "is an Armstrong number.")

else:
    print(original, "is not an Armstrong number.")

print("Thank you!")
