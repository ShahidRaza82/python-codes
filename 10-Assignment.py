
# 1 -- Assignment

security_code = int(input("Enter security code : "))
if security_code == 5566:
    department = input("Enter your department : ")
    if department.lower() == "finance":
        access_level = int(input("Enter your access level : "))
        if access_level >= 5:
            print("Access Granted: Welcome to the meeting room.")
        else:
            print("Insufficient access level. ")
    else:
        print("Access Denied: Department not allowed.")
else:
    print("Invalid security code.")


# 2 -- Assignment
reg_no = int(input("Enter your registration number : "))
if reg_no == 1221:
    exam_sub = input("Enter your subject : ")
    if exam_sub.lower() == 'python':
        password = int(input("Enter your password : "))
        if password == 8888:
            print("Login successful! Start your exam.")
        else:
            print("Wrong password")
    else:
        print("Subject not available.")
else:
    print("Registration failed.")