# Instructions
# Use append() to add Jupiter and Saturn at the end of the list.
# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# Use insert() to add Earth, and Venus in the correct order.
# Use append() again to add Pluto to the end of the list.
# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.



planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

print("planet list", planet_list)

planet_list.extend (["Uranus", "Neptune"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

print("adding Venus and Earth", planet_list)


planet_list.append("Pluto")
print("adding Pluto", planet_list)

#slicing planets starting at index 0 and ending at index 4.
rocky_planets = planet_list[0:4]

print("Rocky planets", rocky_planets)

# print(f"my_randoms list contains {number}")


del planet_list[8]
print (planet_list)








#Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune — and Planet Nine.
#The four rocky planets are Mercury, Venus, Earth and Mars.






