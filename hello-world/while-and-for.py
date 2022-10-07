# decalre var new_planet and planets
new_planet = ""
planets = []

# while loop to add planets to list
while new_planet != "done":
    new_planet = input("Enter a planet(Case Sensitive) or type done to exit: ")
    if new_planet != "done":
        planets.append(new_planet)

# print list with for loop
for planet in planets:
    print(planet)