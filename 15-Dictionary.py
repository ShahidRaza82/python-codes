'''DICTIONARY
Definition - A dictionary is collection of unordered, mutable, 
and indexed key-value pairs enclosed in {} curly braces.

Example - {"name":"Shahid", "age":24, "city":"Aurangabad"}
'''

student = {"name":"Shahid", "age":24, "city":"Aurangabad"}
print(student)

# Accessing values
print("Name : ", student["name"])
print("Age : ", student["age"])
print("City : ", student["city"])



# Adding and updating

#Adding new key-values
student["marks"] = 94
student["Class"] = 7
print("After adding new entry : ", student)

# updating existing value
student["city"] = "Dehradun"
print(student)

# Removing entry
student.pop('age')
print(student)


# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

# Looping
for k in student:
    print(k, student[k])


# Nested Dictionary
employees = {
    "E101": {"name":"Shahid", "city":"Mumbai"},
    "E102": {"name":"Raza", "city":"Jaipur"},
    "E103": {"name":"Raju", "city":"Banglore"}
}
print(employees["E102"]["city"])


# mapper wrong ➡️ correct











