from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
#Solution
def capitalize_letters(item):
    return str.upper(item)

print(list(map(capitalize_letters, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
#Solution
my_numbers.reverse()
print(list(zip(my_strings, my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
#solution
def filter_out(item):
    return item > 50

print(list(filter(filter_out, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
#Solution

def add_numbers(number, score):
    return number + score
print(reduce(add_numbers, (my_numbers + scores)))