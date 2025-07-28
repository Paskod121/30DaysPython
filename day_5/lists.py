# Exercises - Day 5 - Lists

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
my_hobbies = ['reading', 'coding', 'gaming', 'cooking', 'sport', 'music']

# 3. Find the length of your list
length_of_my_hobbies = len(my_hobbies)

# 4. Get the first item, the middle item and the last item of the list
first_item = my_hobbies[0]
middle_item = my_hobbies[len(my_hobbies)//2]
last_item = my_hobbies[-1]

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Pascal', 20, 1.85, 'Single', 'Lomé, Togo']

# 6. Declare a list variable named it_companies and assign initial values
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print("IT Companies list:", it_companies)

# 8. Print the number of companies in the list
print("Number of companies:", len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]
print("First:", first_company, "| Middle:", middle_company, "| Last:", last_company)

# 10. Print the list after modifying one of the companies
it_companies[1] = 'Alphabet'
print("Modified list (Google -> Alphabet):", it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Tesla')
print("After adding Tesla:", it_companies)

# 12. Insert an IT company in the middle of the companies list
middle_index = len(it_companies)//2
it_companies.insert(middle_index, 'Netflix')
print("After inserting Netflix in middle:", it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)

# 15. Check if a certain company exists in the it_companies list
does_exist = 'Apple' in it_companies

# 16. Sort the list using sort() method
it_companies_copy = it_companies.copy()  # To save the original list
it_companies_copy.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies_copy.reverse()

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
middle_start = len(it_companies)//2 - 1
middle_end = len(it_companies)//2 + 2
middle_companies = it_companies[middle_start:middle_end]

# 21. Remove the first IT company from the list
it_companies_temp = it_companies.copy()
it_companies_temp.pop(0)

# 22. Remove the middle IT company or companies from the list
it_companies_temp2 = it_companies.copy()
middle_idx = len(it_companies_temp2)//2
it_companies_temp2.pop(middle_idx)

# 23. Remove the last IT company from the list
it_companies_temp3 = it_companies.copy()
it_companies_temp3.pop()

# 24. Remove all IT companies from the list
it_companies_temp4 = it_companies.copy()
it_companies_temp4.clear()

# 25. Destroy the IT companies list
del it_companies_temp4

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack_temp = front_end + back_end

# 27. Copy the joined list and assign it to variable full_stack, then insert Python and SQL after Redux
full_stack = full_stack_temp.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')

# Exercises: Level 2
# 1. The following is a list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages_sorted = sorted(ages)
min_age = min(ages)
max_age = max(ages)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# Find the median age
ages_for_median = sorted(ages)
n = len(ages_for_median)
if n % 2 == 0:
    median = (ages_for_median[n//2 - 1] + ages_for_median[n//2]) / 2
else:
    median = ages_for_median[n//2]
print("   Median age:", median)

# Find the average age
average_age = sum(ages) / len(ages)
print("   Average age:", average_age)

# Find the range of the ages
age_range = max_age - min_age
print("   Age range:", age_range)

# Compare the value of (min - average) and (max - average), use abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print("   |min - average|:", min_avg_diff)
print("   |max - average|:", max_avg_diff)

# 2. Find the middle country(ies) in the countries list
countries = countries = [
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
n_countries = len(countries)
if n_countries % 2 == 0:
    middle_countries = countries[n_countries//2 - 1:n_countries//2 + 1]
else:
    middle_countries = [countries[n_countries//2]]

# 3. Divide the countries list into two equal lists
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]

# 4. Unpack the first three countries and the rest as scandic countries
countries_to_unpack = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = countries_to_unpack
print("4. China:", china)
print("   Russia:", russia)
print("   USA:", usa)
print("   Scandic countries:", scandic_countries)
