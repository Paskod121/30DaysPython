# Exercises: Day 8  Dictionaries

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'LUOLOU'
dog['color'] = 'Black'
dog['breed'] = 'labrador Retriever'
dog['legs'] = 4
dog['age'] = 3

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys
student = {
    'first_name': 'Pascal',
    'last_name': 'SEWONOU',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'HTML', 'CSS', 'React', 'Node', 'MongoDB'],
    'country': 'Togo',
    'city': 'Lomé',
    'address': {
        'street': '123 Rue de la Paix',
        'tribe': 'ewe'
    }
}

# 4. Get the length of the student dictionary
student_length = len(student)

# 5. Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
skills_data_type = type(skills_value)

# 6. Modify the skills values by adding one or two skills
student['skills'].append('C++')
student['skills'].append('C#')

# 7. Get the dictionary keys as a list
student_keys = list(student.keys())

# 8. Get the dictionary values as a list
student_values = list(student.values())

# 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())

# 10. Delete one of the items in the dictionary
del student['address']

# 11. Delete one of the dictionaries
del dog