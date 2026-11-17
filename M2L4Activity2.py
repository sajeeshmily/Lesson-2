
print("===== CHARACTER OCCURRENCE COUNTER =====")

text = input("Enter a string: ")
ch = input("Enter the character to search: ")

count = 0

for i in text:
    if i == ch:
        count = count + 1

print("Character:", ch)
print("Number of occurrences:", count)
