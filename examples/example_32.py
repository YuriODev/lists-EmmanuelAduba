# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Filter out even numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the result
print(odd_numbers)
