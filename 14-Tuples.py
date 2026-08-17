'''TUPLES
Definition --> A Tuple is an ordered, immutable (unchangeable) collection that stores 
multiple items inside round brackets ().
Example - ('Apple', 'Banana', 'Cherry')
'''

# Create Tuple
fruits = ('Apple', 'Banana', 'Cherry')
print(fruits)

# Indexing
print(fruits[1])
print(fruits[-3])

# Slicing
nums = (10, 20, 30, 40, 50, 60)
print(nums[2:4])

# Looping
colors = ('Red', 'Blue', 'Green')
for c in colors:
    print(c)


# Check length
print(len(colors))

# Concatenation
a = (1, 2)
b = (3, 4)
c = (5, 6)
print(a + b + c)


# Packing and unpacking
data = ("Laptop", 45000, "Black")

# variables for unpacking
product, price, color = data
print(f"Product : {product}, Price: {price}, Colour: {color}")

# packing
# ...........


# Nested Tuples inside list
employees = [('E101', "Rohit", "Pune"), ('E102', "Sneha", "Mumbai")]
for eid, name, city in employees:
    print(eid, name, city)













