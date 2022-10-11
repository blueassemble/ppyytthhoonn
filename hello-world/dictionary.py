# create dictionary planet
planet = {'name': 'Mars',
          'moons': 2}

# print dictionary
print(planet.get('name')+" has "+str(planet.get('moons'))+" moon(s)")

# update dictionary planet with new key 'circumference (km)'
planet['circumference (km)'] = {
    'polar': 6792,
    'equatorial': 6792
}

# print dictionary planet with new key 'circumference (km)'
print(f'{planet.get("name")} has a polar circumference of {planet.get("circumference (km)").get("polar")} km and an equatorial circumference of {planet.get("circumference (km)").get("equatorial")} km')


# create dictionary planet_moons
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

#Obtain a list of moons and number of planets
moons = list(planet_moons.values())

#get total planets
total_planets = len(planet_moons)

#print total planets
print(f'Total planets: {total_planets}')

#get total moons with for loop
total_moons = 0
for moon in moons:
    total_moons += moon
    #get average moons
    average_moons = total_moons / total_planets

#print total moons and average moons
print(f'Total moons: {total_moons} / Average moons: {average_moons}')
