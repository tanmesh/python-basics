# Defining a function
def greet(name):
    """This function greets the person with the given name."""
    print(f"Hello, {name}!")


# Calling the function
greet("Alice")  # Output: Hello, Alice!


# Function with default parameter
def greet_with_default(name="there"):
    """This function greets the person with the given name, defaulting to 'there' if no name is provided."""
    print(f"Hello, {name}!")


# Calling the function with and without providing a name
greet_with_default("Bob")  # Output: Hello, Bob!
greet_with_default()  # Output: Hello, there!


# Function with multiple parameters
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b


# Calling the function
result = add(3, 5)
print(result)  # Output: 8


# Function with variable number of arguments
def add_all(*args):
    """This function adds all the numbers provided as arguments."""
    total = 0
    for num in args:
        total += num
    return total


# Calling the function with different number of arguments
print(add_all(1, 2, 3))  # Output: 6
print(add_all(1, 2, 3, 4, 5))  # Output: 15


# Function with keyword arguments
def create_person(name, age, **kwargs):
    """This function creates a dictionary representing a person with the given name, age, and additional optional information."""
    person = {
        "name": name,
        "age": age
    }
    person.update(kwargs)  # Adding additional key-value pairs
    return person


# Calling the function with keyword arguments
person1 = create_person("Alice", 30, city="New York", occupation="Engineer")
print(person1)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}


# Function with default parameters and keyword arguments
def describe_person(name, age, city="Unknown", **kwargs):
    """This function describes a person with the given name, age, and additional optional information."""
    print(f"{name} is {age} years old and lives in {city}.")
    if kwargs:
        print("Additional Information:")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")


# Calling the function with different arguments
describe_person("Bob", 25)  # Output: Bob is 25 years old and lives in Unknown.
describe_person("Charlie", 40, city="Los Angeles", occupation="Artist")


# Output:
# Charlie is 40 years old and lives in Los Angeles.
# Additional Information:
# - occupation: Artist

# Function with a return statement
def is_even(number):
    """This function checks if the given number is even and returns True or False."""
    return number % 2 == 0


# Using the return value of the function
print(is_even(4))  # Output: True
print(is_even(3))  # Output: False


# Nested function
def outer_function():
    """This function defines an outer function."""
    print("Outer function is called.")

    def inner_function():
        """This function defines an inner function."""
        print("Inner function is called.")

    # Calling the inner function
    inner_function()


# Calling the outer function
outer_function()
# Output:
# Outer function is called.
# Inner function is called.
