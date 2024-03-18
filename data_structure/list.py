# Mutability:
# Lists: Mutable (can be modified after creation)
# Tuples: Immutable (cannot be modified after creation)

# Performance:
# Lists: Generally consume more memory and have slower performance due to mutability
# Tuples: More memory-efficient and faster performance due to immutability

# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# Creating a list of mixed data types
mixed_list = [10, 'hello', 3.14, True]

# Accessing elements of a list using index
print(numbers[0])  # Output: 1
print(fruits[2])   # Output: orange
print(mixed_list[1])  # Output: hello

# Negative indexing: accessing elements from the end of the list
print(numbers[-1])  # Output: 5 (last element)
print(fruits[-2])   # Output: grape (second to last element)

# Slicing a list to get a subset of elements
subset = numbers[1:4]  # Elements from index 1 (inclusive) to 4 (exclusive)
print(subset)  # Output: [2, 3, 4]

# Modifying elements of a list
fruits[1] = 'kiwi'  # Replace 'banana' with 'kiwi'
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape', 'pineapple']

# Adding elements to a list
fruits.append('mango')  # Append 'mango' to the end of the list
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape', 'pineapple', 'mango']

# Inserting elements at a specific position
fruits.insert(2, 'pear')  # Insert 'pear' at index 2
print(fruits)  # Output: ['apple', 'kiwi', 'pear', 'orange', 'grape', 'pineapple', 'mango']

# Removing elements from a list
fruits.remove('orange')  # Remove 'orange' from the list
print(fruits)  # Output: ['apple', 'kiwi', 'pear', 'grape', 'pineapple', 'mango']

# Removing elements by index
removed_element = fruits.pop(3)  # Remove element at index 3 (grape) and return it
print(removed_element)  # Output: grape
print(fruits)  # Output: ['apple', 'kiwi', 'pear', 'pineapple', 'mango']

# Checking if an element exists in a list
print('kiwi' in fruits)  # Output: True
print('banana' in fruits)  # Output: False

# Length of a list
print(len(fruits))  # Output: 5

# Sorting a list
numbers.sort()  # Sorts the list in ascending order
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Reversing a list
fruits.reverse()
print(fruits)  # Output: ['mango', 'pineapple', 'pear', 'kiwi', 'apple']

# Creating a list of lists (2D list or list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6 (accessing element at row 1, column 2)

# List comprehension - creating lists in a concise way
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


