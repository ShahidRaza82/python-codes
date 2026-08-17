# If else conditions

age = int(input("Enter age : "))
if(age>=18):
    print("Can vote")
else:
    print("Cannot vote")


# Discount Checker
amount = int(input("Enter amount : ₹ "))
if(amount >= 1000):
    print("Discount applied 20% ")
    discount = (amount * 20)/100
    print(f"You have to pay only : ₹ {amount - discount}")
else:
    print("You are not eligible for any discount. SORRY!")


# if-elif-else (Multiple conditions)
marks = int(input("Enter your marks : "))
if(marks >= 90):
    print("Grade A")
elif (marks >= 75):
    print("Grade B")
elif (marks >= 50):
    print("Grade C")
else:
    print("Fail")


# String comparison Examples
city = "Delhi"
if city.lower()=="delhi":
    print("City matched")
else:
    print("City not matched")

# Password validation
password = input("Enter your password : ")

if password == "Admin@1":
    print("Login Successful")
else:
    print("Wrong Password")

# Email validation
email = input("Enter your email id : ")

if"@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


# Advance : Missing data check into a String.
original = "Hello, This is Shahid Raza. I am here to learn Python programming."

# handles all international Unicode characters, proper lower case
value = original.casefold() 
verify = value.split()

provide = input("Enter a data to check its availability : ")
check = provide.casefold()
if check in verify:
    print("Data Available")
    print("Index of checked data : ", verify.index(check))
else:
    print("Not found")

print("Printing original data : ", original)
print("Printing case folded original : ", verify)
print("Printing case folded input : ", check)







