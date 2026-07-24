# Input and Typecasting

name = input("Enter your name : ")
print("Your name is : ", name)

age = input("Enter your age : ")
print("Your age is : ", age)

# It consider the number input as String initially.
print("Type of input age is : ", type(age))

# Typecasting converts the data as per requirement.
age = int(age)
print("Type of input age after typecasting is : ", type(age))

age = age + 5
print("New age is : ", age)



# Even the decimal value input is considered as String input.
temperature1 = input("Enter temperature : ")
print("The temperature is : ", temperature1)
print(type(temperature1))

# Another input of temperature by using typecasting.
temperature2 = float(input("Enter temperature : "))
print("The temperature is : ", temperature2)
print(type(temperature2))


# Convert number to string
sale = 5000
# concatenation with (+) plus sign
# type must be same while concatenating.
text = "Total sales : " + str(sale)
print(text)



# Total sales calculator
product = input("Product Name : ")
quantity = int(input("Enter quantity sold : "))
price_per_unit = float(input("Enter price per unit : "))

Total_sale_Amount = quantity * price_per_unit
print("===============================")
print("Product Name : ", product)
print("Quantity sold : ", quantity)
print("Price per unit : ", price_per_unit)
print("Total sales Amount : ", Total_sale_Amount)



# Assignment
# Write a program to generate salary slip (take input -> employee name, basic salary, bonus amount, tax percentage)

employee_name = input("Enter employee name : ")
basic_salary = float(input("Enter basic salary : ₹"))
bonus_amount = float(input("Enter bonus amount : ₹"))
tax_percentage = float(input("Enter tax percentage : %"))

# calculations
gross_salary = basic_salary + bonus_amount
tax_amount = (gross_salary * tax_percentage) / 100
net_salary = gross_salary - tax_amount

# print all the data.
print("================================")
print("Employee Name : ", employee_name)
print("Basic Salary : ₹", basic_salary)
print("Bonus Amount : ₹", bonus_amount)
print("Tax Percentage : %", tax_percentage)
print("Gross Salary : ₹", gross_salary)
print("Tax Amount : ₹", tax_amount)
print("Net Salary (in hand) : ₹", net_salary)








