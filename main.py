from math import pi

if __name__ == "__main__":
    pass

def circle_area(radio):
    if type(radio) not in [int, float]:
        raise TypeError("The radius should be a number")
    elif radio < 0:
        raise ValueError("The radius cannot be negative.")
    else:
        return pi * (radio ** 2)


area_de_un_metro = circle_area(50)
circle_area(90)

 #print(area_de_un_metro)

# Test
# set_de_radios_de_circulos = [2, 3, 0, -6, 5j, True, "radius"]
set_de_radios_de_circulos = [2, 3, 0]

# message = f"Area of circles with r = {radius} is {area}."

for r in set_de_radios_de_circulos:
    A = circle_area(r)
    message = f"Area of circles with r = {r} is {A}."
    #print(message.format(radius=r, area=A))
    #print(message)
