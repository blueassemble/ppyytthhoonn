#create list of planets
planets= ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#print list
print(planets)

#print number of items in list
print("There are", len(planets), "planets in the list")

#add planet to list
planets.append("Pluto")

#print number of planets in list and last planet
print("There are", len(planets), "planets in the list")
print("The last planet is", planets[-1])

#remove planet from list
planets.remove("Pluto")

#prompt user for planet
user_planet = input("Enter a planet(Case Sensitive): ")

#where is planet in list
print(user_planet, "is at index", planets.index(user_planet))

#display planets that is closer to the sun
print("Planets closer to the sun are", planets[0:planets.index(user_planet)])

#display planets that is further from the sun
print("Planets further from the sun are", planets[planets.index(user_planet)+1:])