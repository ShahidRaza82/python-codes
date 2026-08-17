# # For Loop

# # 1. Basic loop

# for i in range(1,11):
#     print(i)


# # 2. Print Characters
# word = "Encyclopedia"
# for alphabet in word:
#     print(alphabet)


# # 3. Print something in repetition n times
# word2 = "Python is interesting."
# for a in range(1, 11):
#     print(a,", "+ word2)

# # 4. For loop with if condition
# word2 = "Python is interesting."
# for a in range(1, 11):
#     print(a,", "+ word2)
#     if a % 2 == 0:
#         print(a)
#     else:
#         print(a,", Odd Hai ye.")


# # 5. Loop through list
# items = ["Pen", "book", "Laptop"]
# for item in items:
#     print(item)

# # 6. Marks calculation
# marks = [78, 81, 89, 76, 92]
# total_marks = 0
# print("Printing marks : ")
# for i in marks:
#     print(i)
#     total_marks += i
# print("Total marks : ", total_marks)

# # 7. Printing numbers with n gap --> range(f, l, g)
# # f --> First number
# # l --> Last number
# # g --> gap between each numbers.

# # Q.1 - Print first n even numbers
# n = int(input("Provide a number : "))
# print("Printing first ", n, " even numbers : ")
# t = n*2
# # method -- 1
# for i in range(2, t+1, 2):
#     print(i)
# # method -- 2
# for i in range(2, t+1):
#     if i % 2 == 0:
#         print(i)


# # Q.2 - Print first n odd numbers
# n = int(input("Provide a number : "))
# print("Printing first ", n, " odd numbers : ")
# t = n*2
# # method -- 1
# for i in range(1, t, 2):
#     print(i)
# # method -- 2
# for i in range(1, t):
#     if i % 2 != 0:
#         print(i)

# # Q.3 - Print Table of n.
# n = int(input("Enter a number to print its table : "))
# print(f"Printing table of : {n}")
# t = n*10
# # method -- 1
# for i in range(n, t+1, n):
#     print(i)
# # method -- 2
# print("Using method 2.")
# for i in range(n, t+1):
#     if i % n == 0:
#         print(i)


# # Q.4 - Print number from 'f' to 'l' with a gap of 'g' between each numbers.
# f = int(input("Enter first number : "))
# l = int(input("Enter last number : "))
# g = int(input("Enter a number to create gap between each numbers : "))
# print(f"Printing numbers from  {f} to {l} with a gap of {g} below :")
# for i in range(f, l+1, g):
#     print(i)


# # 8. Clean city names in list
# cities = ["   MuMbAI", "pUNe      ", "      ChennaI     "]
# cleaned = []
# for i in cities:
#     cleaned.append(i.strip().title())
#     # append() --> add data to the list at very last side by increasing its index by 1.
#     # strip() --> removes spaces before and after of each member.
#     # title() --> makes first letter capital of each member.
# print(cleaned)


# # 9. Extract last 4 digits from IDs
# ids = ['EMP-001122', 'EMP-787986', 'EMP-765788']
# for emp in ids:
#     print("Last 4 digits : ", emp[-4:])


# 10. Work on dictionary
student = {"name":"Shahid", "age":24, "city":"Aurangabad"}
for key, value in student.items():
    print(key, ":", value)


