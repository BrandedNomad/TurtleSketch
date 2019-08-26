import math

def height_of_triangle(half_base):
    height = 0
    full_base = half_base * 2
    height_squared = math.pow(full_base, 2) - math.pow(half_base, 2)
    height = math.sqrt(height_squared)
    return height

x = height_of_triangle(100)
print(x)