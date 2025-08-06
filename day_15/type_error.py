# Day 15 - Python Error Types Practice

# 1. SYNTAX ERROR 
print("SYNTAX ERROR - Missing parentheses, brackets, quotes, etc.")
print("Examples of SyntaxError:")

# print 'hello world'  # Missing parentheses
# if 5 > 3  # Missing colon
# print("hello"  # Missing closing parenthesis

# Correct versions:
print("Correct: print('hello world')")
if 5 > 3:
    print("Correct: if statement with colon")
print("Correct: matching parentheses")

# 2. NAME ERROR 
print("NAME ERROR - Using variables that don't exist")
print("Examples of NameError:")

try:
    print(undefined_variable)  # This will cause NameError
except NameError as e:
    print(f"NameError caught: {e}")

# Fix: Define the variable first
my_name = "Python Learner"
print(f"Fixed: {my_name}")

# 3. INDEX ERROR 
print("INDEX ERROR - Accessing list index that doesn't exist")
print("Examples of IndexError:")

my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}")
print(f"List length: {len(my_list)}")
print(f"Valid indexes: 0 to {len(my_list)-1}")

try:
    print(my_list[10])  # Index 10 doesn't exist
except IndexError as e:
    print(f"IndexError caught: {e}")

# Fix: Use valid index
print(f"Fixed: my_list[2] = {my_list[2]}")

# Safe way to access list elements
def safe_get_item(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range"

print(f"Safe access: {safe_get_item(my_list, 10)}")

# 4. MODULE NOT FOUND ERROR 
print("MODULE NOT FOUND ERROR - Importing non-existent modules")
print("Examples of ModuleNotFoundError:")

try:
    import nonexistent_module  # This module doesn't exist
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError caught: {e}")

# Fix: Import correct module name
import math
print(f"Fixed: Successfully imported math module")
print(f"math.pi = {math.pi}")

# 5. ATTRIBUTE ERROR 
print("ATTRIBUTE ERROR - Using non-existent methods/attributes")
print("Examples of AttributeError:")

try:
    result = math.PI  # Should be 'pi' not 'PI'
except AttributeError as e:
    print(f"AttributeError caught: {e}")

# Fix: Use correct attribute name
print(f"Fixed: math.pi = {math.pi}")

# Another example with string
my_string = "hello world"
try:
    my_string.append("!")  # Strings don't have append method
except AttributeError as e:
    print(f"AttributeError caught: {e}")

# Fix: Use correct string method
print(f"Fixed: my_string + '!' = {my_string + '!'}")

# 6. KEY ERROR 
print("\nKEY ERROR - Accessing non-existent dictionary keys")
print("Examples of KeyError:")

student = {'name': 'Alice', 'age': 20, 'country': 'Finland'}
print(f"Dictionary: {student}")

try:
    print(student['grade'])  # Key 'grade' doesn't exist
except KeyError as e:
    print(f"KeyError caught: {e}")

# Fix: Use existing key or check if key exists
print(f"Fixed: student['name'] = {student['name']}")

# Safe way to access dictionary
grade = student.get('grade', 'Not available')
print(f"Safe access: grade = {grade}")

# 7. TYPE ERROR 
print("\nTYPE ERROR - Operations between incompatible types")
print("Examples of TypeError:")

try:
    result = 5 + "3"  # Can't add int and string
except TypeError as e:
    print(f"TypeError caught: {e}")

# Fix: Convert to same type
print(f"Fixed: 5 + int('3') = {5 + int('3')}")
print(f"Alternative: str(5) + '3' = {str(5) + '3'}")

# Another example
try:
    my_list = [1, 2, 3]
    my_list[1] = "hello"
    total = sum(my_list)  # Can't sum mixed types
except TypeError as e:
    print(f"TypeError caught: {e}")

# Fix: Keep consistent types
numbers = [1, 2, 3]
total = sum(numbers)
print(f"Fixed: sum([1, 2, 3]) = {total}")

# 8. IMPORT ERROR 
print("\nIMPORT ERROR - Importing non-existent function from module")
print("Examples of ImportError:")

try:
    from math import power  # Should be 'pow' not 'power'
except ImportError as e:
    print(f"ImportError caught: {e}")

# Fix: Use correct function name
from math import pow
print(f"Fixed: pow(2, 3) = {pow(2, 3)}")

# 9. VALUE ERROR 
print("\nVALUE ERROR - Correct type but inappropriate value")
print("Examples of ValueError:")

try:
    number = int("12a")  # Can't convert "12a" to integer
except ValueError as e:
    print(f"ValueError caught: {e}")

# Fix: Use valid string for conversion
print(f"Fixed: int('12') = {int('12')}")

# Another example
try:
    import math
    result = math.sqrt(-4)  # Can't get square root of negative number
except ValueError as e:
    print(f"ValueError caught: {e}")

# Fix: Use positive number
print(f"Fixed: math.sqrt(4) = {math.sqrt(4)}")

# 10. ZERO DIVISION ERROR 
print("\n10. ZERO DIVISION ERROR - Dividing by zero")
print("Examples of ZeroDivisionError:")

try:
    result = 10 / 0  # Can't divide by zero
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")

# Fix: Check for zero before dividing
def safe_divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

print(f"Fixed: safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"Safe: safe_divide(10, 0) = {safe_divide(10, 0)}")
