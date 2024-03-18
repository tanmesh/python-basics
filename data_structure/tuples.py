# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple using index
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Negative indexing: accessing elements from the end of the tuple
print(my_tuple[-1])  # Output: 5 (last element)
print(my_tuple[-2])  # Output: 4 (second to last element)

# Slicing a tuple to get a subset of elements
subset = my_tuple[1:4]  # Elements from index 1 (inclusive) to 4 (exclusive)
print(subset)  # Output: (2, 3, 4)

# Tuple packing and unpacking
a = 1
b = 2
c = 3
my_packed_tuple = a, b, c  # Packing variables into a tuple
print(my_packed_tuple)  # Output: (1, 2, 3)

x, y, z = my_packed_tuple  # Unpacking the tuple into variables
print(x, y, z)  # Output: 1 2 3

# Immutable nature of tuples
# Attempting to modify a tuple will result in an error
# my_tuple[0] = 10  # This will raise an error

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Multiplying tuples
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Length of a tuple
print(len(my_tuple))  # Output: 5

# Tuple membership testing
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Using tuples as keys in dictionaries
tuple_key_dict = {(1, 2): 'value1', (3, 4): 'value2'}
print(tuple_key_dict[(1, 2)])  # Output: value1
