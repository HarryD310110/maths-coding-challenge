
# Maths coding challenge!

import sys

# 1) Ask user to enter an integer and store as a variable
#    Bonus points for checking that the input is an integer and raise an exception if not!

value = input("Please Enter An Integer: ")
try:
   value = int(value)
except:
   print('The Value You Entered Is Not An Integer.')
   sys.exit(1)

# 2) Write functions to calculate the square, cube, square root and reciprocal for the given integer

# For example: 

def calc_square(value):
   return value * value

def calc_cube(value):
   return value * value * value

def calc_sqrt(value):
   return value ** 0.5

def calc_recip(value):
   return 1.0 / value

# 3) Call each function by passing the integer variable to each 

# For example:

square = calc_square(value)
cube = calc_cube(value)
sqrt = calc_sqrt(value)
recip = calc_recip(value)

# 4) print the results to screen

print('Square of', value, 'is :', square)
print('Cube of', value, 'is :', cube)
print('Square Root of', value, 'is :', sqrt)
print('Reciprocal of', value, 'is :', recip)
