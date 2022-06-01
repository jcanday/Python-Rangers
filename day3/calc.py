from math import pi

def area():
    length = input("Enter the length of the house in feet: ")
    width = input("Enter the width of the house in feet: ")
    area = int(length) * int(width)
    print(f"The square footage of the house is {area}")

def circ():
    info = input("Enter 'radius' or 'diameter': ")
    if info.lower() == "radius":
        r = input("Enter the radius of the circle: ")
        print("The circumference is: " + str(2 * pi * int(r)))
    elif info.lower() == "diameter":
        d = input("Enter the diameter of the circle: ")
        print("The circumference is: " + str(int(d) * pi))
    else:
        print("invalid input!")
     