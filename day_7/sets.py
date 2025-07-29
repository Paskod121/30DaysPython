# Exercises  Day 7  Sets

# Data 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises level 1

# 1. Find the length of the set it_companies
length_it_companies = len(it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
more_companies = ['Netflix', 'Tesla', 'Spotify']
it_companies.update(more_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')

# 5. What is the difference between remove and discard
# remove() : throws an error if the element does not exist
# discard() : does not throw an error if the element does not exist

# Exercises level 2

# 1. Join A and B
A_union_B = A.union(B)

# 2. Find A intersection B
A_intersection_B = A.intersection(B)

# 3. Is A subset of B
is_A_subset_of_B = A.issubset(B)

# 4. Are A and B disjoint sets
are_A_B_disjoint = A.isdisjoint(B)

# 5. Join A with B and B with A
A_with_B = A.union(B)
B_with_A = B.union(A)

# 6. What is the symmetric difference between A and B
symmetric_diff_A_B = A.symmetric_difference(B)

# 7. Delete the sets completely
del A
del B

# Exercises level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
age_list_length = len(age)
age_set_length = len(age_set)
which_is_bigger = "list" if age_list_length > age_set_length else "set" if age_set_length > age_list_length else "equal"

# 2. Explain the difference between the following data types: string, list, tuple and set
data_types_explanation = {
    'string': 'Texte immutable avec des caractères ordonnés',
    'list': 'Collection ordonnée et modifiable qui accepte les doublons',
    'tuple': 'Collection ordonnée et immutable qui accepte les doublons',
    'set': 'Collection non-ordonnée et modifiable qui refuse les doublons'
}

# 3. How many unique words in the sentence
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
unique_words_count = len(unique_words)