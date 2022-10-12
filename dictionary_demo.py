from cgi import print_arguments
from random import choice, randint


employees = {"John Doe":1970, "Jack Doe":1980, "Jane Doe":1990} # valójában egy set mert nem lehet ismétlődés

print(len(employees))

# nincs rendezettség, sorrend nem lehet index alapján elérni
print(employees["John Doe"])
employees["Bob"] = 1960
print(employees)

del(employees["Bob"])

print(employees.keys) #nevek
print(employees.values) # évszámok

print(list(employees.values()).index(1980))

#kul és érték párok egymás alá

for k in employees.keys():
    print(f"{k} - {employees[k]}")

for k, v in employees.items(): #kulcs és érték párok
    print(f"{k} - {v}")


another_employees = employees.copy() # másolás

print("Catherine" in employees) # False lesz # if in is működik, de csak kulcsra

#Hisztogram vagy grouping
sentence = "Egy aprócska kalapocska, benne csacska macska mocska."

histogram = {}
for c in sentence:
    c = c.lower()
    if c.isalpha():
        if c not in histogram:
            histogram[c] = 1
        else:
            histogram[c] += 1

print(histogram)

# írd ki egy stringben leggyakrabban szereplő szót

words ="apple banana apple raspberry banana apple"
histogram = {}
fruits = words.split() # lista lesz a szavakból
for fruit in fruits:
    if fruit not in histogram:
        histogram[fruit] = 1
    else:
        histogram[fruit] += 1

print(histogram)

max_fruit =""
max_number = 0

for k,v in histogram.items():
    if max_number < v:
        max_number = v
        max_fruit = k

print(max_fruit)


numbers = [1, 3, 5, 7, 9]

fornames =["Doe", "Smith"]
firstnames = ["John", "Jack", "Jane"]
employees = []
for i in range (0, 100):
    forname = choice(fornames)
    firstname = choice(firstnames)
    name = firstname + " " + forname
    salary = randint (100, 500)
    employee = {"name": name, "salary" : salary}
    employees.append(employee)

print(employees)

