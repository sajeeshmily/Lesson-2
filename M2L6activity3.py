
print("===== SPIRAL STAR PATTERN =====")

n = int(input("Enter the size of the spiral: "))

# Create an empty matrix
matrix = [[" " for j in range(n)] for i in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    # Move from left to right
    for i in range(left, right + 1):
        matrix[top][i] = "*"
    top += 2

    # Move from top to bottom
    for i in range(top - 1, bottom + 1):
        matrix[i][right] = "*"
    right -= 2

    # Move from right to left
    if top <= bottom:
        for i in range(right + 1, left - 1, -1):
            matrix[bottom][i] = "*"
        bottom -= 2

    # Move from bottom to top
    if left <= right:
        for i in range(bottom + 1, top - 1, -1):
            matrix[i][left] = "*"
        left += 2

# Display the spiral
for row in matrix:
    print(" ".join(row))
