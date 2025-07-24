# 🟢Exercises: Level 1


# 1. File created 👉 D:\30daysofpython\30DaysPython\day_2\variables.py

# 2. Day 2: 30 Days of python programming

# 3. firstname variable
first_name = "Pascal"

# 4. lastname variable
last_name = "SEWONOU"

# 5. full_name variable
full_name = "Pascal SEWONOU"

# 6. country variable
country = "Togo"

# 7. city variable
city = "Lomé"

# 8. age variable
age = 20

# 9. year variable
year = 2025

# 10. is_true variable
is_true = True

# 11.Multiple variables in one line
name, age, is_challenger = "Pascal", 20, True 


# 🟢 Exercises: Level 2

# 1. Checking datatype of variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_true))
print(type(name), type(age), type(is_challenger))

# 2. finding the length of my first name
print(len(first_name))

# 3. comparing the length of my first name and last name
print(len(first_name) == len(last_name))

# 4. Declaring variables
num_one = 5
num_two = 4

# 5. Adding num_one and num_two and asigning the value to a total
total = num_one + num_two

# 6. Substracting num_two from num_one and asigning the value to diff
diff = num_one - num_two

# 7. Multiplying num_two and num_one and asigning the value to product
product = num_two * num_one

# 8. Dividing num_one by num_two and asigning the value to division
division = num_one / num_two

# 9. Using modulo division to find the remainder of num_two divided by num_one
remainder = num_two % num_one

# 10. Calculating num_one to the power of num_two and asigning the value to exp
exp = num_one ** num_two

# 11. Finding the floor division of num_one divided by num_two and asigning the value to floor_division
floor_division = num_one // num_two

# 12. The radius of a circle is 30 meters.
# 12.i. Calculationg the area of the circle and asigning to area_of_circle 
area_of_circle = 3.14 * 30 * 30 # Area of circle = pi * r^2
#12.ii. Calculationg of the circumference of a circle and asigning to circum_of_circle
circum_of_circle = 2 * 3.14 * 30 # Circumference of circle = 2 * pi * r
# 12.iii. Taking the radius as user input and calculating the area
radius = input("Enter the radius : ")
area_of_circle = 3.14 * float(radius) * float(radius)

# 13. Using input fuction to get and store the user input
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
country = input("Enter your country : ")
age = input("Enter your age : ")

# 14. Running help('keywords') to check for the python reserved words or keywords
help('keywords')