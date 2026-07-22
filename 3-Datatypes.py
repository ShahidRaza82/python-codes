# Learning datatypes in python
# 7 datatypes

# 1. Text Data -- String (str)-> String is used to represent textual data.
# customer_name = "Rohit"
# print("Customer name is ", customer_name)
# print("Customer datatype is : ", type(customer_name))





# 2. Numeric Data -- Stores whole numbers
# 
# 2.1 Integer(Complete number) -> (int)
# rating = 4
# order_quantity = 3
# print("Rating data type : ",rating, type(rating))
# print("Order_Quantity datatype is : ", order_quantity, type(order_quantity))





# 2.2 Float (Decimal) -- Stores decimal values (float)
# order_amount = 76869.865
# print("Order amount data type is : ", type(order_amount))



## THERE IS NO DOUBLE DATA TYPE IN PYTHON.
## FOR ALL THE DECIMAL VALUES THERE IS ONLY ONE DATA TYPE IN PYTHON WHICH IS 'FLOAT'.




# 2.3 Complex numbers -- Stores number with real+imaginary part (complex)
# a = 3+4j
# print("Datatype of a is : ", type(a))
# giving error while putting alphabet in place of 'j', what could be the reason.




# 3. Boolean (True or False)
# is_paid = True
# print(is_paid, type(is_paid))






# 4. Sequence data type

# 4.1 - List data type.
# cities = ["Mumbai", 'Delhi', "Pune", 'Chennai']
# print(cities)
# print(type(cities))
# mutable -> changeable
# List is defined with square brackets




# 4.2 Tuple data type
# dimensions = (1920, 1080)
# print(dimensions)
# print(type(dimensions))
# immutable -> non changeable
# Touple is defined with round brackets




# 4.3 Range data type
# num = range(10) # starts from index 0, because only one input provided in the range,
#                 # and the single input in the range in considered as last index.
# print(list(num))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(type(num))  # here list is not a data type, it is a predefined function of python,

# num = range(1, 10) # starts from index 1, because two inputs are provided in the range separated with comma,
#                    # and in this condition the first input is considered as the index number,
#                    # and the last one considered as last index.
# print(list(num))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(type(num))

# num = range(1, 10+1)

# print(list(num))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(type(num))

# num = range(2, 10, 2)
# print(list(num))  # [2, 4, 6, 8]
# print(type(num))

# num = range(3, 3*10+1, 3)
# print(list(num))  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# print(type(num))





# 5. Dictionary data type (dict)
# a built-in data structure / mutable data type that stores data in key-value pairs, 
# where each unique key maps to a specific value.
# students ={
#     "name" : "shahid",
#     "roll" : 5,
#     "city" : "Aurangabad"
# }
# print(students)
# print(type(students))







# # 6. Sets
# numbers = {1,3,2,3,4,2,5,6,4,7}
# print(numbers) # {1, 2, 3, 4, 5, 6, 7}
#                # Sets automatically discard any repeated values.
# print(type(numbers))
# # numbers.add(12, 13, 14, 14, 15, 19, 18, 17) # this is wrong method to add value to the set



# numbers.add(12) # it takes only one argument to add it to the set.
# print("After adding a new value to the set : ", numbers)
# # After adding a new value to the set :  {1, 2, 3, 4, 5, 6, 7, 12}



# # numbers.update(11, 10, 9, 15, 13, 17, 20) 
# # it will generate an error -> TypeError: 'int' object is not iterable
# #  .update() method in Python expects an iterable object (like a list, tuple, or another set)



# # UPDATE WITH LIST
# numbers.update([11, 10, 9, 15, 13, 17, 20]) 
# print("After updating with list, the set : ", numbers)
# # output -> After updating the set :  {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 17, 20}



# # UPDATE WITH TUPLE
# numbers.update((8, 18, 19)) 
# print("After updating with tuple, the set : ", numbers)
# # After updating the set :  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20}



# # UPDATE WITH ANOTHER SET
# numbers.update({14, 16})
# print("After adding with another tuple, the set : ", numbers)
# # After adding with another tuple, the set :  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# print(numbers)



# REMOVE FROM SET
# numbers.remove(3) # it takes exactly one argument to remove it from the set.
# print(numbers) # 3 removed from the set.



# numbers.discard(12)
# print(numbers) # 12 removed from the set.




# 7. NoneType - No value
remarks = None     # None is the predefined keyword in python, which is kept in NoneType
print(remarks, type(remarks))