"""
Learn about lists
Unlike strings, lists are mutable
You can update, and append elements to it
"""
# use [] to define a list
l = [1, 2, 3]
print("List ", l, type(l))
# A list of objects (any  type)
a = ["apple", "orange", "pear"]
# Access by index notation
print(a, a[1])
# Replace an element
a[0] = "tomatoes"
print(a, a[1])
a[1] = 3.14
print(a, a[1])

# Begin with an empty list
names = []
# Ask user to enter 3 names, and add them to the list
n = 0
while n < 3:
    names.append(input("Enter your name"))
    n += 1
# Display list
print(names)