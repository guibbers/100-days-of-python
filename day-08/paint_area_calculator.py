import math

height = int(input("Height of the wall: "))
width = int(input("Width of the wall: "))
coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover )
    print(f"You'll need {num_of_cans} cans")

paint_calc(height, width, coverage)