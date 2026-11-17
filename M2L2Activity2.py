
print("==============================")
print("       STRING REVERSER")
print("==============================")

text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("Original String:", text)
print("Reversed String:", reverse)

print("Thank you!")
