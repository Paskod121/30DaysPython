# Exercises: Day 13     

# 1. Filter only negative and zero numbers using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print("Negative and zero numbers:", negative_and_zero)

# 2. Flatten list of lists of lists to one dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# Using nested list comprehension to go through 3 levels
flattened = [number for sublist in list_of_lists for inner_list in sublist for number in inner_list]
print("Flattened list:", flattened)

# 3. Create list of tuples with powers pattern
# Pattern: (i, 1, i**1, i**2, i**3, i**4, i**5) for i from 0 to 10
power_tuples = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print("Power tuples:")
for tuple_item in power_tuples:
    print(tuple_item)

# 4. Flatten countries list and format
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# Get first 3 letters of country name for country code
formatted_countries = [[country[0].upper(), country[0][:3].upper(), city.upper()] 
                      for sublist in countries 
                      for country, city in sublist]
print("Formatted countries:", formatted_countries)

# 5. Change countries list to list of dictionaries
country_dicts = [{'country': country[0].upper(), 'city': city.upper()} 
                for sublist in countries 
                for country, city in sublist]
print("Country dictionaries:", country_dicts)

# 6. Change list of names to concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [first_name + ' ' + last_name 
             for sublist in names 
             for first_name, last_name in sublist]
print("Full names:", full_names)

# 7. Lambda function for slope and y-intercept of linear functions
# For slope: m = (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# For y-intercept: b = y - mx (using point-slope form)
y_intercept = lambda x, y, m: y - m * x

print("Lambda functions for linear equations:")
print("Slope between (1,2) and (3,6):", slope(1, 2, 3, 6))
print("Y-intercept with point (1,2) and slope 2:", y_intercept(1, 2, 2))