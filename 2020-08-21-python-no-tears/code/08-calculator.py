# example calculator (addition)

num_1 = input('please enter a number: ')
num_2 = input('please enter another number: ')

# python always receives inputs as strings
# got to convert

num_1 = int(num_1)
num_2 = int(num_2)

answer = num_1 + num_2
print(f'{num_1} + {num_2} = {answer}')