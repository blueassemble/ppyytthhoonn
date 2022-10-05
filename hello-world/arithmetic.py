first_planet = 149597870
second_planet = 778547200

#subtract first_planet from second_planet
distance_km = second_planet - first_planet
print(distance_km)

#convert distance_km to miles
distance_mi = distance_km * 0.621371
print(distance_mi)

#get first_planet and second_planet with prompt
first_planet = int(input("Enter the distance from the sun for the first planet in KM : "))
second_planet = int(input("Enter the distance from the sun for the second planet in KM : "))

#convert first_planet and second_planet to int
first_planet = int(first_planet)
second_planet = int(second_planet)

#subtract first_planet from second_planet abs() returns absolute value to distance_km
distance_km = abs(second_planet - first_planet)
print(distance_km)