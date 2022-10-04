text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
#split text with . as delimiter
sentences = text.split(".")
print(sentences)

#find temperatures in sentences
for sentence in sentences:
    if "temperature" in sentence:
        print(sentence)


####################
name="Ganymade"
planet="Mars"
gravity="1.43"

print("""Gravity Facts about {name}\n---------\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s^2""".format(name=name,planet=planet,gravity=gravity))