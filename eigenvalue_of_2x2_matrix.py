# Program to find eigenvalues of a 2x2 matrix without using numpy or any library

# For a quadratic equation ax2 + bx + c = 0,
# The roots are calculated using the formula, x = (-b ± √(b² - 4ac))/2a

SQUARE = '\u00B2'  # unicode value of square symbol

matrix = []

for _ in range(2):
	matrix.append(list(map(int, input().split())))

a = 1
b = -(matrix[0][0] + matrix[1][1])
c = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

# default sign before b is negative
b_sign = '-'
# if b is negative then change the sign before b to positive and print absolute value of b in equation as (-- = +)
if b < 0:
	b_sign = '+'

# default sign before c is positive
c_sign = '+'
# if c is negative then change the sign before c to negative and print absolute value of c in equation as (-+ = -)
if c < 0:
	c_sign = '-'

# print(f'{"" if a==1 else a}x{SQUARE} {b_sign} {"" if b==1 else abs(b)}x {c_sign} {abs(c)}')  # kept for future program when working with 3d+ matrices

print(f'x{SQUARE} {b_sign} {"" if b==1 else abs(b)}x {c_sign} {abs(c)}')  # if b is 1, then 1 will not be printed with x

square_root_of_discriminant = (b**(2) - 4*a*c)**0.5  # √(b² - 4ac)

negative_factor = (-b - square_root_of_discriminant)/(2*a)  # (-b - √(b² - 4ac))/2a
positive_factor = (-b + square_root_of_discriminant)/(2*a)  # (-b + √(b² - 4ac))/2a

print(negative_factor, positive_factor)
