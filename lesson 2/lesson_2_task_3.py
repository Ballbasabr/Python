import math

def square(side):
    area = side * side
    return math.ceil(area)
side = 5.2
area = square(side)
print("Площадь квадрата со стороной", side, "равна", area)