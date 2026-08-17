'''
SETS
Definition - A set is an unordered, mutable collection that stores unique values only.
Created using {} curly braces.

Example - {"apple", "banana", "mango"}

'''
# 7 entries with few duplicates
fruits = {"Apple", "Banana", "Apple", "Guava", "Orange", "Banana", "Guava"}


# printing the set provide the unique only and eliminate duplicates
print(fruits)
# {'Apple', 'Orange', 'Guava', 'Banana'}

# Add items
fruits.add("Cherry")
print(fruits)

# Remove items
fruits.discard("Guava")
print(fruits)

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5, 6}

print("Union : ", a | b) 
print("Intersection : ", a & b)
print("Difference : ", a - b)
print("Symmetric Diffrence : ", a ^ b)

# Remove duplicates
cities = ["Mumbai", "Pune", "Delhi", "Mumbai"]
unique = set(cities) # cities list converted into set.
print("Unique cities : ", unique)

# Missing values
list1 = {"SQL", "Excel", "Power BI"}
list2 = {"SQL", "Power BI"}
missing = list1 - list2
print("Missing : ", missing)


# Common Skills
deptA = {"SQL", "Excel", "Python"}
deptB = {"Python", "Excel", "Power BI"}
print("Common Skills : ", deptA & deptB)











