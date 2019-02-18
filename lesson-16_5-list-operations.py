#!/usr/bin/env python3

# list-operations.py - summary of basic list operations
#
# Learn:
#     create a list of simple elements
#     display a list
#     create an empty list
#     append an element to a list
#     display number of elements in a list
#     display specific elements of a list
#     display last element of a list
#     iterate over a list
#     create a list of mixed element types
#     create a list of lists
#     display specific elements of a list of lists
#     display number of elements in a list inside a list
#     display specific elements of a list inside a list
#     iterate over a list of lists
#
# Note:
#     Output is shown after '#' while other comments follow '##'

print('>>> create a list of simple elements (from literal values)')
scores1 = [2]
scores3 = [2, 4, 6]
pets1 = ['dog']
pets3 = ['dog', 'cat', 'bird']
propositions1 = [True]
propositions3 = [True, False, True]
print()

print('>>> create a list of simple elements (from variables)')
sm = 'small'
md = 'medium'
lg = 'large'
sizes = [sm, md, lg]
print()

print('>>> display a list')
print(scores1)            # [2]
print(scores3)            # [2, 4, 6]
print(pets1)              # ['dog']
print(pets3)              # ['dog', 'cat', 'bird']
print(propositions1)      # [True]
print(propositions3)      # [True, False, True]
print(sizes)              # ['small', 'medium', 'large']
print()

print('>>> create an empty list')
colors = []
print(colors)             # []
print()

print('>>> append an element to a list')
colors.append('red')
print(colors)             # ['red']
colors.append('green')
print(colors)             # ['red', 'green']
colors.append('blue')
print(colors)             # ['red', 'green', 'blue']
print()

print('>>> display number of elements in a list')
print(len(colors))        # 3
shapes = []
print(len(shapes))        # 0
shapes.append('square')
print(len(shapes))        # 1
shapes.append('circle')
print(len(shapes))        # 2
print()

print('>>> display specific elements of a list')
print(colors[0])          # red
print(colors[1])          # green
print(colors[2])          # blue
print()

print('>>> display last element of a list')
offset = len(colors) - 1
print(colors[offset])     # blue
print()

print('>>> iterate over a list (to print values)')
for color in colors:
    print('color: %s' % color)
print()
# color: red
# color: green
# color: blue

print('>>> iterate over a list (to add values)')
scores_sum = 0
for score in scores3:     ## scores3 = [2, 4, 6]
    scores_sum += score
print(scores_sum)         # 12
print()

print('>>> create a list of mixed element types')
piano = [3, 'piano', 2000 ]   ## quantity, product, cost
drums = [
    2,        ## quantity
    'drums',  ## product
    1000      ## cost
]
guitar = [1, 'guitar', 500]
print(piano)         # [3, 'piano', 2000]
print(drums)         # [2, 'drums', 1000]
print(guitar)        # [1, 'guitar', 500]
print()

print('>>> iterate over a list of lists (to add first element of list in lists)')
instruments = [piano, drums, guitar]
total_quantity = 0
for instrument in instruments:
    total_quantity += instrument[0]
print(total_quantity)  # 6
print()

print('>>> create a list of lists from literals')
days = [
    ['mon', 'tues', 'wed', 'thurs', 'fri'],
    ['sat', 'sun']
]
print(days)          # [['mon', 'tues', 'wed', 'thurs', 'fri'], ['sat', 'sun']]
print()

print('>>> display specific elements of a list of lists')
print(days[0])       # ['mon', 'tues', 'wed', 'thurs', 'fri']
print(days[1])       # ['sat', 'sun']
print()

print('>>> display number of elements in a list inside a list')
print(len(days[0]))  # 5
print(len(days[1]))  # 2
print()

print('>>> display specific elements of a list inside a list')
print(days[0][0])    # mon
print(days[0][1])    # tues
print(days[1][0])    # sat
print(days[1][1])    # sun
print()

print('>>> create a list of lists from variables')
weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
weekends = ['sat', 'sun']
all_days = [weekdays, weekends]
print(all_days)      # [['mon', 'tues', 'wed', 'thurs', 'fri'], ['sat', 'sun']]
print()

print('>>> iterate over a list of lists (to print values)')
for category in days:
    for day in category:
        print('day: %s' % day)
print()
# day: mon
# day: tues
# day: wed
# day: thurs
# day: fri
# day: sat
# day: sun

print('>>> iterate over a list of lists (to print values and number of values)')
for category in days:
    print('%d days' % len(category))
    print('------')
    for day in category:
        print(day)
    print()
# 5 days
# ------
# mon
# tues
# wed
# thurs
# fri
#
# 2 days
# ------
# sat
# sun

print('>>> iterate over a list of lists (to count number of values)')
num_values = 0
for category in days:
    num_values += len(category)
print(num_values)         # 7
print()
