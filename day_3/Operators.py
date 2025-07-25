# 🟢 Exercises - Day 3
import math
# 1. Declaring my age as integer variable
age = 20

# 2. Declaring my height as float variable
height = 1.89

# 3. Declaring a variable that stores a complex number
complex_number = 1 + 3j

# 4. a script that prompts the user to enter base and height of the triangle and calculate the area of the triangle
base = int(input("Enter base : "))
height = int(input("Enter height : "))
area = 0.5 * base * height
print("The area of the triangle is : ", area)

# 5. a script that prompts the user to enter side a, side b, and side c of a triangle and calculate the perimeter of the triangle
side_a = int(input("Enter side a : "))
side_b = int(input("Enter side b : "))
side_c = int(input("Enter side c : "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is : ", perimeter)

# 6. Getting length and width of a rectangle using prompt. Calculating its area and perimeter
length = int(input("Enter length : "))
width = int(input("Enter width : "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is : ", area)
print("The perimeter of the rectangle is : ", perimeter)

# 7. Getting radius of a circle using prompt. Calculating its area and circumference
pi = 3.14
radius = int(input("Enter radius : "))
area = pi * radius ** 2
perimeter = 2 * pi * radius
print("The area of the circle is : ", area)
print("The circumference of the circle is : ", perimeter)

# 8. calculating the slope of X-intercept and y-intercept of y = 2x -2
"""
y = ax + b
slope = a
x_intercept = -b/a
y_intercept = b
"""
x=1;
y = 2 * x - 2
slope_8 = 2
y_intercept_8 = -2
x_intercept_8 = -(y_intercept_8)/slope_8

# 9. Slope is (m = y2-y1/x2-x1). Finding the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope_9 = (y2-y1)/(x2-x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 10. comparing the slapes in tasks 8 and 9
is_slape8_equal_slape9 = slope_8 == slope_9
print("Is slope 8 equal to slope 9 : ", is_slape8_equal_slape9)

# 11. Calculating the value of y (y = x^2 + 6x + 9) and trying to use different x values and figure out at what x value y is going to be 0.
# y = x^2 + 6x + 9
# y = (x + 3)^2
# y = 0
# x + 3 = 0
# x = -3


y = (x ** 2) + (6 * x) + 9

x = -5
print("For x = -5, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = -4
print("For x = -4, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = -3
print("For x = -3, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = -2
print("For x = -2, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = -1
print("For x = -1, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = 0
print("For x = 0, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = 1
print("For x = 1, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = 2
print("For x = 2, The value of y is : ", y)

y = (x ** 2) + (6 * x) + 9
x = 3
print("For x = 3, The value of y is : ", y)

# 12. Finding the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len("python")
dragon_length = len("dragon")
is_python_equal_dragon = python_length == dragon_length

# 13. Using and operator to check if 'on' is found in both 'python' and 'dragon'
is_on_in_python_and_dragon = "on" in "python" and "on" in "dragon"

# 14.  "I hope this course is not full of jargon". Using in operator to check if jargon is in the sentence.
is_jargon_in_sentence = "jargon" in "I hope this course is not full of jargon"

# 15. There is no 'on' in both dragon and python
not_on_in_python_and_dragon = not("on" in "python" and "on" in "dragon")

# 16. Finding the length of the text python and convert the value to float and convert it to string
python_length = len("python")
python_length_float = float(python_length)
python_length_string = str(python_length)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number : "))
is_even = number % 2 == 0
print("Is the number even : ", is_even)

# 18. Checking if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division = 7 // 3
int_value = int(2.7)
is_equal = floor_division == int_value
print("Is the floor division of 7 by 3 equal to the int converted value of 2.7 : ", is_equal)

# 19 checking if type of '10' is equal to type of 10
is_equal = type('10') == type(10)
print("Is type of '10' equal to type of 10 : ", is_equal)

# 20 Checking if int('9.8') is equal to 10
is_equal = int(float('9.8')) == 10
print("Is int('9.8') equal to 10 : ", is_equal)

# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours : "))
rate_per_hour = int(input("Enter rate per hour : "))
pay = hours * rate_per_hour
print("Pay of the person : ", pay)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years : "))
seconds = years * 365 * 24 * 60 * 60
print("Number of seconds a person can live : ", seconds)

# 23. Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")