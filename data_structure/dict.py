# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@example.com"
}

# Accessing elements of a dictionary using keys
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30

# Modifying elements of a dictionary
my_dict["age"] = 35  # Updating the value associated with the "age" key
print(my_dict["age"])  # Output: 35

# Adding new elements to a dictionary
my_dict["occupation"] = "Engineer"
print(my_dict["occupation"])  # Output: Engineer

# Removing elements from a dictionary
del my_dict["email"]
# Alternatively, you can use the pop() method to remove and return the value
# removed_email = my_dict.pop("email")
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'occupation': 'Engineer'}

# Checking if a key exists in a dictionary
print("name" in my_dict)  # Output: True
print("email" in my_dict)  # Output: False

# Length of a dictionary (number of key-value pairs)
print(len(my_dict))  # Output: 4

# Getting all keys or values of a dictionary
print(my_dict.keys())    # Output: dict_keys(['name', 'age', 'city', 'occupation'])
print(my_dict.values())  # Output: dict_values(['John', 35, 'New York', 'Engineer'])

# Iterating over keys and values of a dictionary
for key in my_dict:
    print(key, "->", my_dict[key])

# Iterating over keys and values of a dictionary
for key, value in my_dict.items():
    print(key, "->", value)

# Clearing a dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Creating a dictionary with different data types as values
person = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "grades": [90, 85, 88],
    "address": {
        "city": "Los Angeles",
        "zipcode": "90001"
    }
}

# Accessing nested elements in a dictionary
print(person["grades"][0])  # Output: 90
print(person["address"]["city"])  # Output: Los Angeles
