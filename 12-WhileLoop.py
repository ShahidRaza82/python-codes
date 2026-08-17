# While Loop

# 1. Basic while loop
i = 1
while i<=5:
    print(i)
    i+=1


# Ask user input until valid input
num = ""
while not num.isnumeric():
    num = input("Enter any value : ")
    print("Please enter only number.")
print("Number accepted : ", num)



# Using break in while loop
x = 1
while x <= 10:
    print(x)
    if x == 5:
        break
    x+=1


# Using continue in while loop
y = 0
while y < 10:
    y += 1
    if y % 2 == 0:
        continue
    print(y)



# Password System with attempts limit.
password = ""
attempts = 0

while password != "Admin@123" and attempts < 3:
    password = input("Enter your password : ")
    attempts += 1
    if password == "Admin@123":
        print("Login Successful ✅")
    else:
        print("Wrong Password ❌")
        if attempts < 3:
            print(f"Try Again! Attempts left : {3 - attempts}")
        else:
            print("No attempts left. You can login later.")
            print("Your account is blocked for 24 hours.")


















