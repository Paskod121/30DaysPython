# Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
concatenated_string = "Thirty" + " " + "Days" + " " + "Of" + " " + "Python"

# 2. Concatenate the string 'Coding', 'For' 'All' to a single string, 'Coding For All'
concatenated_string = "Coding" + " " + "For" + " " + "All"

# 3. Declare a variable named company and assign it the value 'Coding For All'
company = "Coding For All"

# 4. Print the variable company using print()
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
to_uppercase = company.upper()

# 7. Change all the characters to lowercase letters using lower() method.
to_lowercase = company.lower()

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
to_capitalize = company.capitalize()
to_title = company.title()
to_swapcase = company.swapcase()

# 9. Cut(slice) out the first word of Coding For All string
first_word = company[0:6]

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
is_contain = "Coding" in company

# 11. Replace the word 'Coding' in the string 'Coding For All' to Python
replace_word = company.replace("Coding", "Python")

# 12. Change 'Python for Everyone' to 'Python for All' using the replace() method.
replace_word = company.replace("Everyone", "All")

# 13. Split the string 'Coding For All' using space as a separator (split())
split_word = company.split(" ")

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
split_word = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(",")

# 15. What is the character at index 0 in the string 'Coding For All' using char_at() or square bracket method
char_at_0 = company[0]

# 16.What is the last index of the string Coding For All
last_index = company.rindex("l")

# 17. What is the character at index 10 in the string 'Coding For All' string
char_at_10 = company[10]

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = "Python For Everyone".split(" ")[0][0] + "Python For Everyone".split(" ")[1][0] + "Python For Everyone".split(" ")[2][0]

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
acronym = "Coding For All".split(" ")[0][0] + "Coding For All".split(" ")[1][0] + "Coding For All".split(" ")[2][0]

# 20. Use index to determine the position of the first occurrence of C in Coding For All
first_occurrence = company.index("C")

# 21. Use index to determine the position of the first occurrence of F in Coding For All
first_occurrence = company.index("F")

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
last_occurrence = company.rfind("l")

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = "You cannot end a sentence with because because because is a conjunction".index("because")

# 24. Use rindex or rfind to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_occurrence = "You cannot end a sentence with because because because is a conjunction".rindex("because")

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = "You cannot end a sentence with because because because is a conjunction"[22:55]

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = "You cannot end a sentence with because because because is a conjunction".index("because")

# 27. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_occurrence = "You cannot end a sentence with because because because is a conjunction".rindex("because")

# 28. Does 'Coding For All' start with a substring Coding?
is_start = company.startswith("Coding")

# 29. Does 'Coding For All' end with a substring coding?
is_end = company.endswith("coding")

# 30. '   Coding For All      '  Remove the left and right trailing spaces in the string
remove_spaces = "   Coding For All      ".strip()

#31.Which one of the following variables return True when we use the method isidentifier():
isidentifier_1 = "30DaysOfPython".isidentifier()
isidentifier_2 = "thirty_days_of_python".isidentifier()

#32.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_libraries = " #".join(libraries)

#33. Use the new line escape sequence to separate the following sentences.
sentences = "I am enjoying this challenge.\nI just wonder what is next."

#34. Use a tab escape sequence to write the following lines.
sentences = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"

#35. 35. Use the string formatting method to display the following:
"""radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square."""

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius", radius, "is", area, "meters square")

#36. Make the following using string formatting methods:
"""8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""

num_1 = 8
num_2 = 6
print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
print("{} / {} = {}".format(num_1, num_2, num_1 / num_2))
print("{} % {} = {}".format(num_1, num_2, num_1 % num_2))
print("{} // {} = {}".format(num_1, num_2, num_1 // num_2))
print("{} ** {} = {}".format(num_1, num_2, num_1 ** num_2))
