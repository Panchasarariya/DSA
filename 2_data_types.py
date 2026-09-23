#Data Types
#1. Demonstrate int, float, str, bool, and complex.
a = 10
b = 10.5
c = "Hello"
d = True
e = 3 + 4j

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

#2. Accept two numbers and display their data types.
a = input("Enter first number: ")
b = input("Enter second number: ")

print("First number:", a)
print("Data type:", type(a))

print("Second number:", b)
print("Data type:", type(b))

#3. Convert a string number into an integer and float.
num = "25"

integer_num = int(num)
float_num = float(num)

print("Integer:", integer_num)
print("Type:", type(integer_num))

print("Float:", float_num)
print("Type:", type(float_num))

#4. Find the length of a string
text = "Hello Python"

length = len(text)

print("String:", text)
print("Length:", length)

#5. Create a list, tuple, set, and dictionary and display their types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"name": "Riya", "age": 20}

print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dict)
print("Type:", type(my_dict))
 
