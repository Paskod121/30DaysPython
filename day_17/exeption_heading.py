# 🟢 Exercises - Day 17
# 1. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Using unpacking with * operator to separate the list
finland, sweden, norway, denmark, iceland, es, ru = names

# Creating nordic_countries list with the first 5 countries
nordic_countries = [finland, sweden, norway, denmark, iceland]

# Alternative way using unpacking with *rest pattern
# *nordic_countries, es, ru = names
# This would put the first 5 in nordic_countries automatically