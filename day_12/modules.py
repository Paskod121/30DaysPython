# Exercises: Day 12 Modules

# Importing modules we need
from random import random, randint
import string

# Exercises: Level 1

# 1. Generate a six digit/character random user ID
def random_user_id():
    # Characters we can use: letters and numbers
    characters = string.ascii_letters + string.digits
    user_id = ""
    
    for i in range(6):
        # Pick a random character
        random_index = randint(0, len(characters) - 1)
        user_id += characters[random_index]
    
    return user_id

# 2. Generate user IDs based on user input for length and count
def user_id_gen_by_user():
    # Get user input
    num_chars = int(input("Number of characters: "))
    num_ids = int(input("Number of IDs: "))
    
    characters = string.ascii_letters + string.digits
    
    for i in range(num_ids):
        user_id = ""
        for j in range(num_chars):
            random_index = randint(0, len(characters) - 1)
            user_id += characters[random_index]
        print(user_id)

# 3. Generate RGB color values (0-255 for each)
def rgb_color_gen():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    
    return "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ")"

# Exercises: Level 2

# 1. Generate any number of hexadecimal colors
def list_of_hexa_colors(num_colors):
    hexa_colors = []
    hexa_chars = "0123456789abcdef"
    
    for i in range(num_colors):
        hexa_color = "#"
        for j in range(6):
            random_index = randint(0, len(hexa_chars) - 1)
            hexa_color += hexa_chars[random_index]
        hexa_colors.append(hexa_color)
    
    return hexa_colors

# 2. Generate any number of RGB colors
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    
    for i in range(num_colors):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        rgb_color = "rgb(" + str(red) + ", " + str(green) + ", " + str(blue) + ")"
        rgb_colors.append(rgb_color)
    
    return rgb_colors

# 3. Generate colors based on type (hexa or rgb)
def generate_colors(color_type, num_colors):
    if color_type == "hexa":
        return list_of_hexa_colors(num_colors)
    elif color_type == "rgb":
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'"

# Exercises: Level 3

# 1. Shuffle a list randomly
def shuffle_list(lst):
    # Create a copy so we don't modify the original
    shuffled = []
    original_copy = []
    
    # Make a copy of the original list
    for item in lst:
        original_copy.append(item)
    
    # Randomly pick items from the copy until it's empty
    while len(original_copy) > 0:
        random_index = randint(0, len(original_copy) - 1)
        shuffled.append(original_copy[random_index])
        # Remove the picked item
        new_copy = []
        for i in range(len(original_copy)):
            if i != random_index:
                new_copy.append(original_copy[i])
        original_copy = new_copy
    
    return shuffled

# 2. Generate seven unique random numbers (0-9)
def seven_random_numbers():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    
    # Pick 7 unique numbers
    for i in range(7):
        random_index = randint(0, len(numbers) - 1)
        result.append(numbers[random_index])
        # Remove the picked number to ensure uniqueness
        new_numbers = []
        for j in range(len(numbers)):
            if j != random_index:
                new_numbers.append(numbers[j])
        numbers = new_numbers
    
    return result
