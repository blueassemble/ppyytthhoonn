sum = 1 + 2
print(sum)

print("show this in the console")

sum = 1 + 2 # 3
product = sum * 2
print(product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

type(distance_to_alpha_centauri)

left_side = 10
right_side = 5
left_side / right_side # 2

from datetime import date
print(date.today())

print("Today's date is: " + str(date.today()))


print(date.today())

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")