# Halmaz = set összevissza vannak az elemek, míg a listában egy definiált sorrendben

numbers = {1, 2, 3}
print(numbers)

numbers = {1, 2, 3, 1, 2, 3}
print(numbers) # ugyanaz lesz ugyanis a halmaz nem enged duplikációt

numbers = {1, 2}
numbers.add(3)
print(numbers)

set1 = {1,2,3,4}
set2 = {4, 5, 6}

print(set1 | set2) # unió
print(set1 & set2) # metszet
print(set1 - set2) # kivonás

set1 = {4, 5, 6}
set1 = {1,2,3,4,5,6}

print(set1.issubset(set2)) # set1 minden eleméttartalmazza a set2-nek
print(set2.issuperset(set1))

set3 = frozenset(set1) #létrehoz egy új setet de az módosíthatatlan (listánál a tupple)
# set3.add(3)

numbers = [1,2,3,4,1,2,3,4]
set1 = set(numbers)
print(set1)


letters = ["a", "b", "c", "a", "b", "c"]

def different_letters(letters): # hány különböző karakter van
    return len(set(letters))

print(different_letters(letters))