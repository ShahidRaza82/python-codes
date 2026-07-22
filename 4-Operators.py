# 1. Arithmetic Operators (+, -, *, /)
num1 = 40
num2 = 8

print("First number : ", num1)
print("Second number : ", num2)

print("Sum : ",(num1+num2))
print("Subtraction : ", (num1-num2))
print("Multiplication : ", (num1*num2))
print("Division : ", (num1/num2))
print("Floor Division : ", (num1//num2))
print("Modulus -> Remainder : ", (num1%num2))
print("Exponent : ", (num1**num2))


# 2. Assignment Operators (=, +=, -=, *=, /=, and more...)
value = 10 # The value 10 assigned to the variable 'value'.
print("Original : ", value)
value+=10
print("After += ", value)

value-=10
print("After -= ", value)

value*=10
print("After *= ", value)

value/=10
print("After /= ", value)



# 3. Comparison Operators (==, !=, >, <, >=, <=)
# Returns boolean data (True/False)
a = 15
b = 13
print("Equal to check : ", a==b) 
print("Not equal to check : ", a!=b)
print("Greater than check : ", a>b)
print("Less than check : ", a<b)
print("Greater than or Equal to check : ", a>=b)
print("Less than or equal to check : ", a<=b)



# 4. Logical Operators (and, or, not)
x = 25
y = 5
print(y<=x and x>y)
print((x!=pow(y, 2)) or x<y)
print(not((x>y) and (x!=pow(y, 2))))
print(not((x==pow(y, 2)) or (x<y)))



# 5. Identity Operators (is, is not)
m1 = 100
m2 = 100
print(m1 is m2)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
print(type(x)," and ", type(y))

print(hex(id(x)))
print(hex(id(y)))



# 6. Membership Operator (in, not in)  --> boolean return type
# --> Checks if a value (case sensitive) exists inside a sequence like (list, tuple, String)

print("Check 'a' in Shahid Raza : ", 'a' in "Shahid Raza")
print("Check 'a' in Mango : ", 'a' in "Mango")

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)


# 7. Ternary Operator

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)


num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)








