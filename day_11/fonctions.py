# Exercises: Day 11 Functions

# 1.Declare a function add_two_numbers. It takes two parameters and it returns a sum
def add_two_numbers(num1, num2):
    return num1 + num2

# 2. Aire d'un cercle
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area

# 3. Additionner tous les nombres (nombre arbitraire d'arguments)
def add_all_nums(*nums):
    # Vérifier si tous les éléments sont des nombres
    for num in nums:
        if type(num) != int and type(num) != float:
            return "Erreur: Tous les éléments doivent être des nombres"
    
    total = 0
    for num in nums:
        total += num
    return total

# 4. Convertir Celsius en Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 5. Vérifier la saison selon le mois
def check_season(month):
    month = month.lower()
    if month == 'décembre' or month == 'janvier' or month == 'février':
        return 'Winter'
    elif month == 'mars' or month == 'avril' or month == 'mai':
        return 'Spring'
    elif month == 'juin' or month == 'juillet' or month == 'août':
        return 'Summer'
    elif month == 'septembre' or month == 'octobre' or month == 'novembre':
        return 'Autumn'
    else:
        return 'Mois invalide'

# 6. Calculer la pente d'une équation linéaire
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

# 7. Résoudre une équation quadratique ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    discriminant = b * b - 4 * a * c
    
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Pas de solution réelle"

# 8. Afficher chaque élément d'une liste
def print_list(lst):
    for item in lst:
        print(item)

# 9. Inverser une liste (avec des boucles)
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 10. Mettre en majuscule les éléments d'une liste
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.upper())
    return capitalized_lst

# 11. Ajouter un élément à la fin d'une liste
def add_item(lst, item):
    new_lst = []
    for element in lst:
        new_lst.append(element)
    new_lst.append(item)
    return new_lst

# 12. Supprimer un élément d'une liste
def remove_item(lst, item):
    new_lst = []
    for element in lst:
        if element != item:
            new_lst.append(element)
    return new_lst

# 13. Somme des nombres de 0 à n
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

# 14. Somme des nombres impairs de 0 à n
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 1:
            total += i
    return total

# 15. Somme des nombres pairs de 0 à n
def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total


# ========== EXERCISES LEVEL 2 ==========

# 1. Compter les nombres pairs et impairs de 0 à n
def evens_and_odds(n):
    evens_count = 0
    odds_count = 0
    
    for i in range(n + 1):
        if i % 2 == 0:
            evens_count += 1
        else:
            odds_count += 1
    
    print("The number of odds are " + str(odds_count) + ".")
    print("The number of evens are " + str(evens_count) + ".")

# 2. Calculer la factorielle d'un nombre
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

# 3. Vérifier si quelque chose est vide
def is_empty(item):
    if item == "" or item == [] or item == {} or item == () or item == None:
        return True
    return False

# 4. Fonctions statistiques pour les listes

# Moyenne
def calculate_mean(lst):
    if len(lst) == 0:
        return 0
    
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

# Médiane
def calculate_median(lst):
    if len(lst) == 0:
        return 0
    
    # Trier la liste (méthode débutant avec boucles)
    sorted_lst = []
    for num in lst:
        sorted_lst.append(num)
    
    # Tri à bulles simple
    for i in range(len(sorted_lst)):
        for j in range(len(sorted_lst) - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                temp = sorted_lst[j]
                sorted_lst[j] = sorted_lst[j + 1]
                sorted_lst[j + 1] = temp
    
    middle = len(sorted_lst) // 2
    if len(sorted_lst) % 2 == 0:
        return (sorted_lst[middle - 1] + sorted_lst[middle]) / 2
    else:
        return sorted_lst[middle]

# Mode (valeur qui apparaît le plus souvent)
def calculate_mode(lst):
    if len(lst) == 0:
        return None
    
    # Compter les occurrences
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Trouver la valeur avec le plus d'occurrences
    max_count = 0
    mode_value = lst[0]
    
    for num in counts:
        if counts[num] > max_count:
            max_count = counts[num]
            mode_value = num
    
    return mode_value

# Étendue (range)
def calculate_range(lst):
    if len(lst) == 0:
        return 0
    
    min_val = lst[0]
    max_val = lst[0]
    
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return max_val - min_val

# Variance
def calculate_variance(lst):
    if len(lst) == 0:
        return 0
    
    mean = calculate_mean(lst)
    total = 0
    
    for num in lst:
        total += (num - mean) ** 2
    
    return total / len(lst)

# Écart-type
def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5

# Exercises: Level 3

# 1. Vérifier si un nombre est premier
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# 2. Vérifier si tous les éléments d'une liste sont uniques
def all_items_unique(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True

# 3. Vérifier si tous les éléments ont le même type
def same_data_type(lst):
    if len(lst) == 0:
        return True
    
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True

# 4. Vérifier si c'est un nom de variable Python valide
def is_valid_python_variable(name):
    # Doit être une chaîne
    if type(name) != str:
        return False
    
    # Ne peut pas être vide
    if len(name) == 0:
        return False
    
    # Premier caractère doit être une lettre ou _
    first_char = name[0]
    if not ((first_char >= 'a' and first_char <= 'z') or 
            (first_char >= 'A' and first_char <= 'Z') or 
            first_char == '_'):
        return False
    
    # Les autres caractères doivent être lettres, chiffres ou _
    for char in name[1:]:
        if not ((char >= 'a' and char <= 'z') or 
                (char >= 'A' and char <= 'Z') or 
                (char >= '0' and char <= '9') or 
                char == '_'):
            return False
    
    # Ne peut pas être un mot-clé Python
    keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 
                'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 
                'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
                'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 
                'while', 'with', 'yield']
    
    if name in keywords:
        return False
    
    return True

# Tests Level 2 et 3
if __name__ == "__main__":
    print("\n=== TESTS LEVEL 2 ===")
    evens_and_odds(100)
    print("Factorial 5:", factorial(5))
    print("Is empty '':", is_empty(""))
    print("Is empty [1,2]:", is_empty([1,2]))
    
    test_list = [1, 2, 3, 4, 5, 5, 6]
    print("Mean:", calculate_mean(test_list))
    print("Median:", calculate_median(test_list))
    print("Mode:", calculate_mode(test_list))
    print("Range:", calculate_range(test_list))
    print("Variance:", calculate_variance(test_list))
    print("Std:", calculate_std(test_list))
    
    print("\n=== TESTS LEVEL 3 ===")
    print("Is 17 prime:", is_prime(17))
    print("Is 15 prime:", is_prime(15))
    print("All unique [1,2,3]:", all_items_unique([1,2,3]))
    print("All unique [1,2,2]:", all_items_unique([1,2,2]))
    print("Same type [1,2,3]:", same_data_type([1,2,3]))
    print("Same type [1,'a',3]:", same_data_type([1,'a',3]))
    print("Valid variable 'my_var':", is_valid_python_variable('my_var'))
    print("Valid variable '2var':", is_valid_python_variable('2var'))