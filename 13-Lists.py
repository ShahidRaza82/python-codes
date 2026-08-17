'''
LIST

Definition --> A 'list' is an ordered, mutable(changeable) collection that can
store multiple values of different data types.

Example:- [item1, "item2", item3]
* under square brackets.
here - item1, and item3 show numeric value
but item2 shows textual value because it is in inverted commas.

Q. Why Lists are important for Data Analysts?
Ans. Lists are the foundation of handling tabular data before Pandas.
'''

# Create list
fruits = ["Apple", "Banana", "Mango"]
print(fruits)



# Indexing
print(fruits[0]) # print value kept at index 0 in the list --> Apple
print(fruits[-1]) # print value kept at index -1 in the list --> Mango



# Updating list value
fruits[1] = "Orange" # properly change the value kept the specified index.
# ['Apple', 'Banana', 'Mango']
# ['Apple', 'Orange', 'Mango']
print(fruits)



# Add items
fruits.append("Grapes") # increase size of the list by increasing its index by 1, 
# and keep the value at last index.

# ['Apple', 'Banana', 'Mango']
# ['Apple', 'Banana', 'Mango', 'Grapes']
print(fruits)

fruits.insert(1, "Papaya") # it also increases size of the list by increasing its index by 1, 
# and then shift all the values by +1 index, and then put value at provided index.

# ['Apple', 'Banana', 'Mango', 'Grapes']
# ['Apple', 'Papaya', 'Banana', 'Mango', 'Grapes']
print(fruits)



# Remove items
fruits.remove("Mango")
# ['Apple', 'Banana', 'Mango']
# ['Apple', 'Banana']
print(fruits)

fruits.pop() # If we don't provide index to pop, its default index behavior is -1
# value at index -1 is removed
# ['Apple', 'Banana']
# ['Apple']
print(fruits) 

# To check its functionality with providing index first we put some values to the list
fruits.append("Cherry")
fruits.append("Grapes")
fruits.append("Orange")

# ['Apple', 'Banana', 'Mango']
# ['Apple', 'Banana', 'Mango', 'Cherry', 'Grapes', 'Orange']
print(fruits)

fruits.pop(-2) # item at index -2 is removed
# ['Apple', 'Banana', 'Mango', 'Cherry', 'Grapes', 'Orange']
# ['Apple', 'Banana', 'Mango', 'Cherry', 'Orange']
print(fruits)

fruits.pop(2) # item at index 2 is removed
# ['Apple', 'Banana', 'Mango', 'Cherry', 'Orange']
# ['Apple', 'Banana', 'Cherry', 'Orange']
print(fruits)


# Looping in fruits
for f in fruits:
    print("Fruits : ", f)



# SLICING
nums = [10, 20, 30, 40, 50, 60]
print(nums[:3]) # Starting index is not provided so default is 0.
# prints a new sliced list from index 0 to provided last -1 (3-1 = 2 --> 0, 1, 2)
# [10, 20, 30]

print(nums[-3:]) # Starting index is provided and last is not, so its default is last index.
# prints a new sliced list from index -3 to default index last which is -1. (-3, -2, -1)
# [40, 50, 60]


# Clean the city names
raw = ["     MumBaI     ", "deLHi       ", "    PunE"]
clean =[] # taking an empty list variable.
for c in raw:
    # putting values in clean [] list one by one by removing spaces and making first letter capital for each value
    clean.append(c.strip().title())
print(clean)
# ['Mumbai', 'Delhi', 'Pune']



# Replace items
fixed = [] # taking an empty list variable.
for c in clean:
    c = c.replace("Mumbai", "Hydrabad").replace("Delhi", "Chennai").replace("Pune", "Bengalore")
    fixed.append(c)
print(fixed)
# ['Mumbai', 'Delhi', 'Pune']
# ['Hydrabad', 'Chennai', 'Bengalore']



# Extract specified data.
codes = ['Laptop-2024', 'Phone-2023']
years = [] # empty list
for c in codes:
    years.append(c[-4:])
print(years)















