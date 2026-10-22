
"""Practice program for loops and number patterns."""

# Display numbers from 1 to 10 using a while loop
print("Counting from 1 to 10:")
count = 1

while count <= 10:
    print(count, end=" ")
    count += 1

# Display odd numbers using a for loop
print("\n\nOdd numbers between 1 and 50:")
for value in range(1, 51, 2):
    print(value, end=" ")

# Calculate the sum of natural numbers
print("\n\nCalculate the sum of natural numbers:")
try:
    limit = int(input("Enter a positive integer: "))

    if limit < 1:
        print("Please enter a number greater than zero.")
    else:
        result = sum(range(1, limit + 1))
        print(f"Sum of numbers from 1 to {limit}: {result}")

except ValueError:
    print("Invalid input. Please enter a whole number.")

# Print a simple star pattern
print("\nStar pattern:")
for row in range(1, 6):
    print(" " * (5 - row) + "*" * row)

# Generate a multiplication table
print("\nMultiplication table:")
try:
    table_number = int(input("Enter a number for its table: "))

    for multiplier in range(1, 11):
        product = table_number * multiplier
        print(f"{table_number} x {multiplier} = {product}")

except ValueError:
    print("Please enter a valid integer.")
