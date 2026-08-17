# STRING METHODS (VERY IMPORTANT)

text = "            hello shahid Raza            "

print("Original text : ", text)

# Remove Spaces (first and last)
print("Spaces removed : ", text.strip())

# Convert to capital letters text
print("Uppercase text : ", text.upper().strip())

# Convert to proper case
print("Proper Letters : ", text.title().strip())

# Convert to lower letters text
print("Lower case : ", text.lower().strip())

# Replace word
print("Replace hello with 'Hi' : ", text.replace("hello","Hi").strip())

# Counting letter
# --> This will print text without inverted comma.
print("Counting of 'a' in "+text.strip()+" : ",text.count("a")) 

# --> With single inverted comma -- both will print same output
print("Counting of 'a' in '"+text.strip()+"' : ",text.count("a"))
print(f"Counting of 'a' in '{text.strip()}' : {text.count("a")}")

text1 = text.strip()
print(f"Removed Spaces :  {text1}")

# Check if text starts with something
# --> Python is case sensitive language, there for
# it will provide different outputs if text case change in checking.
print(f"Starts with hello? :{text1.startswith("H")}") #--> False
print(f"Starts with hello? :{text1.startswith("h")}") #--> True


# Checking if input is numeric or not.
mobile = '9876543210'
print(type(mobile))

# The isnumeric() method does not check the data type. 
# It checks whether every character in the string is a numeric character.
print(f"Is numeric ? : {mobile.isnumeric()}")

print("123".isnumeric())         # True
print("٠١٢٣".isnumeric())        # True (Arabic numerals)

print("-123".isnumeric())    # False ('-' is not numeric)
print("123.45".isnumeric())  # False ('.' is not numeric)
print("12 34".isnumeric())   # False (space is not numeric)
print("123abc".isnumeric())  # False (letters are present)
print("".isnumeric())        # False (empty string)

mobile1 = int(mobile)
print(type(mobile1))
# Check for fractional part in integer.
#--> if available it returns -- false.
print("Is Integer ? : ", mobile1.is_integer())


# Split text into list of words
message = "Hello, This is Shahid Raza. I am learning Python programming."
print(type(message)) # str

# using split function
text = message.split()
print(type(text)) # --> list
print("Using split() function on text : ", text)
# output --> ['Hello,', 'This', 'is', 'Shahid', 'Raza.', 'I', 'am', 'learning', 'Python', 'programming.']

# it can be directly put into a print function
print(f"Using split() function on text : {type(message.split())}:")

# Join back the splitted message --> from list to str.
print("Joining back the list by separatd with spaces : ", " ".join(text)) # --> contents of list separated by spaces.
print("Joining back the list by separated with hyphen : ", "-".join(text)) # --> contents of list separated by hyphens.

joined_message = " ".join(text)
print(joined_message)


# Finding position of letters
print("Index of 'S': ", joined_message.find('S'))
print("Index of 'Q': ", joined_message.find('Q')) # -1

# Extract domain from email id
email = "shahid@example.com"
print("Email : ", email)
print("Taking domain only : ", email[email.find('@')+1:])

