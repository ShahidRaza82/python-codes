# Nested IF and Multiple conditions

print("Checking your Eligiblity")
age = int(input("Enter your age : "))
if(age >= 18):
    id_no = int(input("Enter your ID number : "))
    if(id_no == 5443):
        print("You can enter 🙏.")
    else:
        print("Invalid ID number. You are not allowed")
else:
    print("You are under age.")




# Multiple conditions with 'and'
age = int(input("Enter your age : "))
citizenship = input("Are you an Indian? : ")

if age >= 18 and citizenship.lower() == 'yes':
    print("Can vote in India")
else:
    print("Cannot vote in India")



