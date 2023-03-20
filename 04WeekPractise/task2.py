#2.Write the program to sort the list (without using sort function). You can implement any algorithm
# Loop function

cities = ["Vilnius","Riga","Talin","Warsaw","Stocholm","Madrid"]
cities_sorted = []

while cities:
    min = cities[0]  
    for i in cities: 
        if i < min:
            min = i
    cities_sorted.append(min)
    cities.remove(min)    

print(cities_sorted)


