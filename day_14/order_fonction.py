# Day 14 - Higher Order Functions Exercises

# Import reduce from functools
from functools import reduce

# Given data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# EXERCISES LEVEL 1

# 1. Explain the difference between map, filter, and reduce
print("Differences between map, filter, and reduce:")
print("- MAP: Transforms each element in a list and returns a new list of same size")
print("- FILTER: Keeps only elements that meet a condition, returns smaller/same size list")
print("- REDUCE: Combines all elements into a single value")

# 2. Explain the difference between higher order function, closure and decorator
print("\nDifferences between higher order function, closure, decorator:")
print("- HIGHER ORDER FUNCTION: Function that takes other functions as parameters")
print("- CLOSURE: Inner function that can access variables from outer function")
print("- DECORATOR: Function that adds functionality to another function")

# 3. Define call functions before map, filter or reduce
def make_uppercase(country):
    return country.upper()

def is_even(num):
    return num % 2 == 0

def add_numbers(x, y):
    return x + y

# 4. Use for loop to print each country
print("\nCountries using for loop:")
for country in countries:
    print(country)

# 5. Use for loop to print each name
print("\nNames using for loop:")
for name in names:
    print(name)

# 6. Use for loop to print each number
print("\nNumbers using for loop:")
for number in numbers:
    print(number)

# EXERCISES LEVEL 2

# 1. Use map to create uppercase countries
uppercase_countries = list(map(make_uppercase, countries))
print("Uppercase countries:", uppercase_countries)

# 2. Use map to square numbers
def square_number(num):
    return num ** 2

squared_numbers = list(map(square_number, numbers))
print("Squared numbers:", squared_numbers)

# 3. Use map to uppercase names
uppercase_names = list(map(make_uppercase, names))
print("Uppercase names:", uppercase_names)

# 4. Filter countries containing 'land'
def contains_land(country):
    return 'land' in country.lower()

land_countries = list(filter(contains_land, countries))
print("Countries with 'land':", land_countries)

# 5. Filter countries with exactly 6 characters
def has_six_chars(country):
    return len(country) == 6

six_char_countries = list(filter(has_six_chars, countries))
print("Countries with 6 characters:", six_char_countries)

# 6. Filter countries with 6 or more characters
def has_six_or_more_chars(country):
    return len(country) >= 6

six_plus_countries = list(filter(has_six_or_more_chars, countries))
print("6. Countries with 6+ characters:", six_plus_countries)

# 7. Filter countries starting with 'E'
def starts_with_e(country):
    return country[0].upper() == 'E'

e_countries = list(filter(starts_with_e, countries))
print("Countries starting with 'E':", e_countries)

# 8. Chain map, filter, reduce operations
# Example: square even numbers then sum them
chained_result = reduce(add_numbers, 
                       list(map(square_number, 
                               list(filter(is_even, numbers)))))
print("Chained operations (sum of squares of even numbers):", chained_result)

# 9. Function to get only string items from a list
def get_string_lists(lst):
    def is_string(item):
        return type(item) == str
    
    return list(filter(is_string, lst))

mixed_list = [1, 'hello', 2, 'world', 3.5, 'python']
string_only = get_string_lists(mixed_list)
print("String items only:", string_only)

# 10. Use reduce to sum all numbers
total_sum = reduce(add_numbers, numbers)
print("Sum of all numbers:", total_sum)

# 11. Use reduce to concatenate countries
def concatenate_countries(country1, country2):
    return country1 + ', ' + country2

countries_sentence = reduce(concatenate_countries, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries'
print("Concatenated sentence:", countries_sentence)

# 12. Function to categorize countries by pattern
def categorize_countries(pattern):
    countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
    def has_pattern(country):
        return pattern.lower() in country.lower()
    
    return list(filter(has_pattern, countries))

print("Countries with 'land' pattern:", categorize_countries('land'))
print("Countries with 'ia' pattern:", categorize_countries('ia'))

# 13. Dictionary with starting letters and counts
def countries_by_starting_letter():
    letter_count = {}
    
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    
    return letter_count

letter_counts = countries_by_starting_letter()
print("Countries count by starting letter:", letter_counts)

# 14. Get first ten countries
def get_first_ten_countries():
    return countries[:10]  

first_ten = get_first_ten_countries()
print("First ten countries:", first_ten)

# 15. Get last ten countries  
def get_last_ten_countries():
    return countries[-10:]  

last_ten = get_last_ten_countries()
print("Last ten countries:", last_ten)

