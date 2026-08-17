'''
Built-in functions --> Built-in functions are pre-defined functions
in Python that help perform operations quickly and efficiently on 
Strings, Lists, and Numbers.

Built-in functions are like shortcuts in python.
Instead of writing long code, Python gives readymade
tools to use.

Example - Instead of counting items manually, use len()
Instead of finding max value manually use max()
'''

# String function
text = "Banana are healthy for health"
print(text.count('a')) # 6

print("hello.py".endswith(".py")) # True

print("Sales_report.csv".startswith("Sales")) # True

print("123".isnumeric()) # True
print("abc".isalpha())   # True
print("12ABC3".isalnum())# True

print("Line1\nLine2\nLine3")
print("Line1\nLine2\nLine3".splitlines())


# List functions
nums = [5, 2, 7, 4, 1, 8, 3]
nums.sort()  # makes in sorted order.
print(nums)

fruits = ["Banana", "Apple", "Mango", "Cherry"]
# fruits.sort()
print(sorted(fruits))

marks = [78, 89, 84, 75, 92]
print(min(marks), max(marks), sum(marks))

mylist = [1, 2, 1, 4, 3, 2, 1, 4, 1, 1, 3, 4, 5]
print(mylist.count(1))  # total number of 1 present in list.
print(mylist.index(3))  # first appearance of 3 at which index.

a = [1, 2, 3]
b = [3, 4, 5, 6]
a.extend(b)  # no duplicates removed while extending
print(a)


# Number functions
print(round(3.678, 2))  # round figure value exact 2 digits after decimal
print(abs(-50))  # absolute value always in positive
print(pow(3, 4)) # 3 to the power 4 --> 3 * 3 * 3 * 3 = 81
print(divmod(10, 3)) # shows quotient and remainder in form of (3, 1)
print(sum([5, 5, 5], 5)) # shows total sum (values of list and outside it) = 20

# Practical example
product = ["  mobile  ", "Laptop", "    Tablet"]
clean = [p.strip().title() for p in product]
clean.sort()
print(clean)


emails = ['shahid@gmail.com', 'hamzah@yahoo.com']
domains = [mail[mail.find('@')+1:] for mail in emails]
print(domains)


# Both the codes given bolow are same.
# 1.
mobile = ['8987654789', '9090008667', '678DVDDC67', '633572']
valid = []
for m in mobile:
    if m.isdigit() and len(m) == 10:
        valid.append(m)
print(valid)

# 2.
mobile = ['8987654789', '9090008667', '678DVDDC67', '633572']
valid = [m for m in mobile if m.isdigit() and len(m) == 10]
print(valid)






