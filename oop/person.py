class Person:
    """A class representing a person."""

    # Constructor method (__init__)
    def __init__(self, name, age):
        """Initialize the person with a name and age."""
        self.name = name
        self.age = age

    # Method to greet the person
    def greet(self):
        """Greet the person."""
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

    # Method to update the age of the person
    def update_age(self, new_age):
        """Update the age of the person."""
        self.age = new_age


# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes of the instance
print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30

# Calling methods of the instance
person1.greet()  # Output: Hello, my name is Alice and I'm 30 years old.

# Updating the age of the person
person1.update_age(35)
print(person1.age)  # Output: 35

person1.greet()  # Output: Hello, my name is Alice and I'm 30 years old.

# Creating another instance of the Person class
person2 = Person("Bob", 25)
person2.greet()  # Output: Hello, my name is Bob and I'm 25 years old.
