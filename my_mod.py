def find_area():
    length = int(input('What is the length of the house?'))
    width = int(input('What is the width of the house?'))
    house_area = length * width
    print(str(house_area) + ' ' + 'sq. feet')
    

from math import pi

def find_circumference():
    diameter = int(input('What is the diameter of the circle?'))
    circumference = diameter * pi
    print(circumference)

find_circumference()
