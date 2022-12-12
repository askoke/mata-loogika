import math

"""Practice different math axpressions and calculations."""

# declare num_a and num_b

num_a = 5
num_b = 2

# 1. Sum and difference

sum = num_a + num_b
print(f"{num_a} + {num_b} = {sum}")

difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")

print('------------------------------------------')

# 2. Float division

division_float = num_a / num_b
print(f"{num_a} / {num_b} = {division_float}")

print('------------------------------------------')

# 3. Integer division

division_int = num_a // num_b
print(f"{num_a} // {num_b} = {division_int}")

print('------------------------------------------')

# 4. Powerful operations

multiply_numbers = num_a * num_b
power = num_a ** num_b
remainder = num_a % num_b
print(f"{num_a} * {num_b} = {multiply_numbers}")
print(f"{num_a} ** {num_b} = {power}")
print(f"{num_a} % {num_b} = {remainder}")

print('------------------------------------------')

# 5. find average

average = (num_b + num_b) / 2
print(f"({num_a} + {num_b}) / 2 = {average}")

print('------------------------------------------')

# 6. Area of circle

radius = 3
circle_area = round(math.pi * (radius ** 2), 2)
print(f"pi * {radius} ** 2 = {circle_area}")

print('------------------------------------------')

# 7. Area of an equilateral triangle

side_length = 5
triangle_area = round(math.sqrt(3) * ((side_length ** 2) / 4) ,0)
print(f"squareroot 3 * ({side_length} ** 2 / 4) = {triangle_area}")

print('------------------------------------------')

# 8. Calculate discriminant

a = 3
b = 6
c = 4
discriminant = (b ** 2) - (4 * a * c)
print(f"({b} ** 2) - (4 * {a} * {c}) = {discriminant}")

print('------------------------------------------')

# 9. Calculate hypotenuse length

a = 3
b = 4
c = math.sqrt(a ** 2) + math.sqrt(b ** 2)
print(f" squareroot (({a} ** 2) + ({b} ** 2)) = {c}")

print('------------------------------------------')

# 10. Calculate cathetus length

c = 10
a = 6
b = math.sqrt(c ** 2) - math.sqrt(a ** 2)
print(f" squareroot (({c} ** 2) - ({a} ** 2)) = {b}")

print('------------------------------------------')
# 11. Time converter

seconds = 149032
minutes = seconds // 60
seconds_left = seconds % 60
hours = minutes // 60
minutes_left = minutes % 60
print(f"{hours} hours, {minutes} minutes, {seconds_left} seconds left, {minutes_left} minutes left")

print('------------------------------------------')

# 12. Student helper

angle = 67
sine = round(math.sin(angle), 1)
cosine = round(math.cos(angle), 1)
print(f"sine of angle 67 is {sine} and cosine is {cosine}")

print('------------------------------------------')

# 13. Greetings

n = 7
lots_of_heys = "Hey" * n
print(lots_of_heys)

print('------------------------------------------')

# 14. Adding numbers

string_numbers = str(num_a) + str(num_b)
print(string_numbers)