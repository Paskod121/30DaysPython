# Exercises  Day 9 Conditionals

# Exercises: Level 1

# 1. Age check for driving
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to learn to drive.")

# 2. Compare ages
my_age = 20
your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print(f"You are {difference} year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print(f"You are {difference} year younger than me.")
    else:
        print(f"You are {difference} years younger than me.")
else:
    print("We are the same age.")

# 3. Compare two numbers
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2

# 1. Grade system
score = int(input("Enter your score: "))

if score >= 80 and score <= 100:
    grade = 'A'
elif score >= 70 and score <= 89:
    grade = 'B'
elif score >= 60 and score <= 69:
    grade = 'C'
elif score >= 50 and score <= 59:
    grade = 'D'
elif score >= 0 and score <= 49:
    grade = 'F'
else:
    grade = 'Invalid score'

print(f"Your grade is {grade}")

# 2. Season check
month = input("Enter a month: ").lower()

if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Invalid month'

print(f"The season is {season}")

# 3. Fruit list check
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input("Enter a fruit: ").lower()

if fruit_input in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit_input)
    print(f"Modified list: {fruits}")

# Exercises: Level 3

person = {
    'first_name': 'SEWONOU',
    'last_name': 'Pascal',
    'age': 20,
    'country': 'Togo',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Lomé',
        'zipcode': '00000'
    }
}

# Check if person has skills key and print middle skill
if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    middle_skill = skills_list[middle_index]
    print(f"Middle skill: {middle_skill}")

# Check if person has Python skill
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill")
    else:
        print("The person does not have Python skill")

# Developer type check
if 'skills' in person:
    skills = person['skills']
    
    if len(skills) == 2 and 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')

# Marriage and country check
if person.get('is_married') == True and person.get('country') == 'Togo':
    first_name = person['first_name']
    last_name = person['last_name']
    country = person['country']
    print(f"{first_name} {last_name} lives in {country}. He is married.")