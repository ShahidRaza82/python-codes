# String Indexing

name = "Shahid"
print(name)

# forward indexing -> left to right (starts with 0)
print(name[0]) # print -> S
print(name[4]) # print -> i

# backward indexing -> right to left (start with -1)
print(name[-1]) # print -> d
print(name[-6]) # print -> S


# String Slicing
product = "Macbook Pro 2024"
print("Provided String : ", product)

# length of the String using len() --> (counts characters as well as spaces available in the string).
print("Length of the string : ", len(product)) # 16

# forward slicing -> within a range -- positively (lower to higher)
print("Forward slicing : ", product[0:7]) # Macbook

# Extracting first 11 characters from the given string
print("First 11 characters : ", product[0:11]) # --> it includes spaces also.

# backward slicing -> within a range -- negetively (higher to lower)
print("Backward slicing 1 : ", product[-16:-8]) # Macbook
print("Backward slicing 2 : ", product[-8:-1]) # Pro 202
print("Backward slicing 3 : ", product[-8:]) # Pro 2024
print("Backward slicing 4 : ", product[-8:0]) # prints nothing.

# WITH GAP
# ==========
print("slicing with character gap : ", product[::3]) # start to end with gap of 3.
print("slicing with character gap : ", product[0::3]) # start to eand with gap of 3.
# both the print functions are providing the same outputs.

# Reversed String
print("Reversed String : ", product[::-1])


