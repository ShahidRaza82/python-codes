'''
RANGE AND LOOPS
* range () generates a sequence of integers.
* Used mostly with for loops.

Syntax - range(start, stop, step)
'''

for i in range(1, 6): 
    print(i) # 1 to 5 printed vertically.

for i in range(5, 11):
    print(i) # 5 to 10 printed vertically.

for i in range(0, 20, 2):
    print(i)  # 0 to 18 printed.

for i in range(2, 21, 2):
    print(i) # table of 2 printed.

# Countdown
for i in range(20, 0, -1):
    print(i)


# Loop through list using index.
items = ["Pen", "Book", "Laptop"]
for i in range(len(items)):
    print(i, items[i])


# Generate employee id
for i in range(1, 6):
    print(f"EMP-{i}")


# Create years list
years = []
for y in range(2015, 2026):
    years.append(y)
print(years)


# Clean cirty names using range
cities = [" MumBaI", " DElHi  ", "pune"]
for i in range(len(cities)):
    cities[i] = cities[i].strip().title()
print(cities)

# Extract last 4 digits from ids
ids = ["EMP-123456", "EMP-980983", "EMP-780087", "EMP-367837"]
for i in range(len(ids)):
    print(ids[i][-4:])


for i in range(1, 4):
    for j in range(1, 4):
        print(f"i value: {i}, j value: {j}")
















