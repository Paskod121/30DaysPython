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
