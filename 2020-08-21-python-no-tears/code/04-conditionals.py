# conditionals are if/else statements
# conditionals are how computers make decisions
# lhs < rhs : less than
# lhs > rhs : greater than 
# lhs <= rhs : less than or equal to
# lhs >= rhs : greater than or equal to
# lhs == rhs : is equal to

age = 19

if age < 18:
    print('minor')
elif age < 25:
    print('young adult')
elif age < 60:
    print('adult')
else:
    print('senior')

# another example

light = 'green'

if light == 'green':
    print('go')
elif light == 'yellow':
    print('slow down')
else:
    print('stop')
