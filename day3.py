#to find absolute value
num = float(input("Enter a number: "))
absolute_value = abs(num)
print("Absolute value is:", absolute_value)


#to find nearest number for decimal
num = 10.678342
round(num)


#to find nearest number of decimal2
num = 9.4567239
round(num,2)


#to find power of a number
base = int(input("Enter a number: "))
exponent = int(input("Enter a number: "))
print("result= ",pow(base, exponent))


#max value and min value
num = [2,57,69,8]
print(max(num))
print(min(num))


#sum of list
num = [1,2]
print(sum(num))


#length
x = ("Mango")
print(len(x))


#length of list
x = [10,20,30,40]
print(len(x))


#convert inter into string
num = 100
string_num = str(num)
print("Integer:", num)
print("String:", string_num)
print("Type after conversion:", type(string_num))


# Convert a string into an integer using int()
num = "100"
integer_num = int(num)
print("String:", num)
print("Integer:", integer_num)
print("Type after conversion:", type(integer_num))


# Convert an integer into a floating-point number using float()
num = 100
float_num = float(num)
print("Integer:", num)
print("Float:", float_num)
print("Type after conversion:", type(float_num))


#type
x = 20
y = 'numbert'
print(type(x))
print(type(y))


#binary and hexadecimal
x = 100
print(bin(x))
print(hex(x))


# Convert a number into octal using oct()
num = 100
octal = oct(num)
print("Number:", num)
print("Octal:", octal)


# Find the Unicode value of a character using ord()
ch = 'k'
print("Character:", ch)
print("Unicode value:", ord(ch))


# Find the character of a Unicode value using chr()
unicode_value = int(input("Enter a Unicode value: "))
print("Character:", chr(unicode_value))


#to check whether a value is true or false using bool
value = input("Enter a value: ")
print("Boolean value:", bool(value))


#program to sort a list of numbers using sorted().
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_list = sorted(numbers)
print("Sorted list:", sorted_list)


#to reverse a list using 
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
reversed_list = list(reversed(numbers))
print("Reversed list:", reversed_list)


#to printt numbers 1 to 10
for i in range(1, 11):
    print(i)


#the index and value of list elements using enumerate()
items = input("Enter list elements separated by space: ").split()
for index, value in enumerate(items):
    print("Index:", index, "Value:", value)

#combine 2 list
list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()
combined = list(zip(list1, list2))
print("Combined list:", combined)

#Apply a function to all elements of a list using map()
numbers = list(map(int, input("Enter numbers: ").split()))
squares = list(map(lambda x: x * x, numbers))
print("Squared values:", squares)

#Filter even numbers from a list using filter()
numbers = list(map(int, input("Enter numbers: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#Check if all elements in a list are true using all()
values = [1, True, "Hello", 5]
print("All elements are true:", all(values))

#Check if any element in a list is true using any()
values = [0, False, "", 5]
print("Any element is true:", any(values))

#Find the length of a tuple using len()
t = tuple(input("Enter tuple elements separated by space: ").split())
print("Length of tuple:", len(t))

#Find the largest number in a user-given list using max()
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
largest = max(numbers)
print("Largest number:", largest)

#Find the smallest number in a user-given list using min()
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
smallest = min(numbers)
print("Smallest number:", smallest)

# Calculate the total marks of students using sum()
marks = list(map(int, input("Enter marks separated by space: ").split()))
total = sum(marks)
print("Total marks:", total)

# Calculate the absolute difference between two numbers using abs()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
difference = abs(num1 - num2)
print("Absolute difference:", difference)

# Calculate the square of a number using pow()
num = int(input("Enter a number: "))
square = pow(num, 2)
print("Square:", square)

# Calculate the cube of a number using pow()
num = int(input("Enter a number: "))
cube = pow(num, 3)
print("Cube:", cube)

# Round a floating-point value to three decimal places
num = float(input("Enter a floating-point number: "))
print("Rounded value:", round(num, 3))

# Convert user input into an integer using int()
num = int(input("Enter an integer: "))
print("Integer value:", num)

# Convert user input into a float using float()
num = float(input("Enter a floating-point number: "))
print("Float value:", num)

# Display the type of multiple variables using type()
a = 10
b = 5.5
c = "Python"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Count the number of characters in a sentence using len()
sentence = input("Enter a sentence: ")
print("Number of characters:", len(sentence))

#Find the highest temperature from a list using max()
temperatures = list(map(int, input("Enter temperatures separated by space: ").split()))
highest = max(temperatures)
print("Highest temperature:", highest)

# Find the lowest price from a list using min()
prices = list(map(float, input("Enter prices separated by space: ").split()))
lowest = min(prices)
print("Lowest price:", lowest)


# Remove false values from a list using filter()
values = [0, 1, False, True, "", "Python", None, 5]
result = list(filter(bool, values))
print("List after removing false values:", result)


# Create a list of squares using map()
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)


# Create a dictionary from two lists using zip()
keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()
dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)


# Display numbers in reverse order using range()
for i in range(10, 0, -1):
    print(i)

# Convert a decimal number into binary, octal, and hexadecimal formats
num = int(input("Enter a decimal number: "))
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))


# Check whether a list contains any positive values using any()
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = any(x > 0 for x in numbers)
print("Contains positive value:", result)


# Check whether all numbers in a list are positive using all()
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = all(x > 0 for x in numbers)
print("All numbers are positive:", result)


# Use multiple built-in functions together to process a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sorted List:", sorted(numbers))
print("Largest Number:", max(numbers))
print("Smallest Number:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))
