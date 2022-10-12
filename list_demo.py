numbers = [2,6,8,12,6]

for number in numbers:
    print(number)

print(numbers [3])

# Slicing
print(numbers[1:4]) #balról zárt, jobbról nyílt a 4es indexű már nincs benne
print(number[1:4:2]) # minden másodikat
print(numbers[::-1]) # lista visszafelé
numbers[1:3] = [66, 77]


print(len(numbers))


#nem javasolt
# egymásba ágyazhatóság
employee = ["john Doe"], 1970, ["blue", "Yellow"]

print([1,2,3]) + [3,4,5] #listához csak listát lehet konkatenálni

print([1,2] * 3) # 3x ismétli a listát

print(12 in numbers)

numbers.append(4) # lista végéhez egy 4

print(type(numbers)) #list class
print(type(3)) #list int

del(numbers[3]) # kitörli a 3. elemet

names = ["John Doe", "Jane Doe", "Jack Doe"]

names.reverse() #módosítja a lista tartalmát
print(names)


print(names[::-1]) #nem módosítja a listát

print(names.index("Jane Doe")) # megkeresi, hogy hányadik a listában

names.sort() #abc sorrend ANGOL abc sorrend ASCI kód szerint
print(names)

names = ["John Doe", "Jane Doe", "Jack Doe"]
names.insert(1, "Bob") # beszúrja Bobot

print(names.count("Jack Doe")) # megszámolja hányszor van

names.remove("Jack Doe") # kitörli az első előfordulást

# while al minden előfordulását törölni


