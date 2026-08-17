'''
FUNCTIONS
Definition - A function is a reusable block of code defined
using 'def' keyword that performs task and optionally returns
a value using return


A function takes input, performs action, and gives an output.

Syntax of function:-
def function_name():
    # code in side the function...

'''

def greet(): # function defined
    print("Hello, I am learning python.")
    print("Learning function in python.")
greet() # function called.


def welcome(name): # parameterized / argumented function.
    print("Welcome ", name)
welcome("Shahid") # prints --> Welcome Shahid


def two_var(a, b):
    print("a + b: ", a+b)
    print("a - b: ", a-b)
    print("a * b: ", a*b)
two_var(2, 7)


def add(a, b):
    return a+b

def multiply(x):
    return x*3

result = add(30, 7)
result2 = multiply(result)
 
print(result)
print(result2)


def clean_text(value):
    return value.strip().title()

output = clean_text("         ShahID RaZA       ")
print(output)


def fix_city(city):
    city = city.lower().strip()
    city = city.replace("mombaii", "mumbai")
    city = city.replace("kolkatta", "kolkata")

    return city.title()
print(fix_city("        mombaii        "))


def get_year(code):
    return code[-4:]
print(get_year("Laptop-2024"))



def is_valid_email(email):
    return '@' in email and '.' in email

print(is_valid_email('shahid@example.com'))




def stats(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

print(stats([30, 20, 10]))



def clean_list(values):
    cleaned =[]
    for v in values:
        cleaned.append(v.strip().title())
    return cleaned
print(clean_list(["   DelHI  ", "    MuMBai    ", "   pUNe       "]))















