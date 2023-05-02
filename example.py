# Example Python script to demonstrate control flow statements and data structures

# Example 1: for loop
print("Example 1: for loop")
for i in range(1, 6):
    print(i)
print()

# Example 2: while loop
print("Example 2: while loop")
i = 1
while i <= 5:
    print(i)
    i += 1
print()

# Example 3: if-else statement
print("Example 3: if-else statement")
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
print()

# Example 4: if-elif-else statement
print("Example 4: if-elif-else statement")
y = 7
if y < 0:
    print("y is negative")
elif y == 0:
    print("y is zero")
else:
    print("y is positive")
print()

# Example 5: dictionary
print("Example 5: dictionary")
my_dict = {
    "apple": 3,
    "banana": 2,
    "orange": 1
}
print(my_dict["apple"]) # access value by key
my_dict["pear"] = 4    # add a new key-value pair
del my_dict["banana"]  # delete a key-value pair
print(my_dict)
print()

# Example 6: tuple
print("Example 6: tuple")
my_tuple = ("apple", "banana", "orange")
print(my_tuple[1])     # access element by index
print(len(my_tuple))   # get length of tuple
print()

# Example 7: list comprehension
print("Example 7: list comprehension")
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)
print()

# Example 8: try-except statement
print("Example 8: try-except statement")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
print()

# Example 9: with statement
print("Example 9: with statement")
with open("example.txt", "w") as f:
    f.write("Hello, world!")
print()

# Example 10: class
print("Example 10: class")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")
    
my_dog = Dog("Fido", 3)
my_dog.bark()
print()

# Example 11: function with default argument
print("Example 11: function with default argument")
def greet(name="world"):
    print(f"Hello, {name}!")
    
greet()         # no argument, uses default
greet("Alice")  # uses provided argument
