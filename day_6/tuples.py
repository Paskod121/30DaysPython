# Exercises: Day 6

print("EXERCISES LEVEL 1\n")

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of my sisters and brothers
brothers = ('Regis', 'Kossi', 'Gilles')
sisters = ('Pascaline', 'Abidé')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
number_of_siblings = len(siblings)
print("Number of siblings:", number_of_siblings)

# 5. Modify the siblings tuple and add the name of my father and mother and assign it to family_members
parents = ('Richard', 'Alice') # Since tuples are immutable, we need to create a new tuple
family_members = siblings + parents
print("Family members:", family_members)

print("\nEXERCISES LEVEL 2\n")

# 1. Unpack siblings and parents from family_members
# We know we have 5 siblings and 2 parents
regis, kossi, gilles, pascaline, abide, richard, alice = family_members
print("Unpacked family members:")
print("   Siblings:", regis, kossi, gilles, pascaline, abide)
print("   Parents:", richard, alice)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to food_stuff_tp
fruits = ('banana', 'orange', 'mango', 'lemon', 'apple')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)
print("Length:", len(food_stuff_tp))

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
length = len(food_stuff_lt)
if length % 2 == 0:
    # Even number of items, take two middle items
    middle_start = length // 2 - 1
    middle_end = length // 2 + 1
    middle_items = food_stuff_lt[middle_start:middle_end]
else:
    # Odd number of items, take one middle item
    middle_index = length // 2
    middle_items = food_stuff_lt[middle_index]


# Also from tuple
if len(food_stuff_tp) % 2 == 0:
    middle_start = len(food_stuff_tp) // 2 - 1
    middle_end = len(food_stuff_tp) // 2 + 1
    middle_items_tp = food_stuff_tp[middle_start:middle_end]
else:
    middle_index = len(food_stuff_tp) // 2
    middle_items_tp = food_stuff_tp[middle_index]

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print("Is Estonia a nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country  
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is Iceland a nordic country?", is_iceland_nordic)
