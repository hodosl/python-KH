# Tuple unpacking
names =("John Doe", "jack Doe")
name1, name2 = names
print(name1)
print(name2)

names = ("John", "Jack", "Bob", "Otto")
i = 0
for name in names:
    print(str(i) + " " + name)

#for i in range len(names):
#    print(f"{i} - {names[i]}")

for i, name in enumerate(names):
    print(f"{i} - {name}")

#employees = [("John Doe", 1970) ("Jane Doe", 1980), ("Jack Doe", 1990)]
#for name, year_of_birth in employees:
#    print(f"{name}: - {year_of_birth}")

orders = [("Vértes", 20), ("Mátra", 30), ("Gerecse", 15)]
sum_orders = 0
for name, m3 in orders:
    sum_orders += m3
print(f"Öszzesen: - {sum_orders}")

max_name = " "
max_amount = 0
for name, m3 in orders:
    if m3 > max_amount:
        max_amount = m3
        max_name = name
print(f"A legtöbbet {max_name} teröletén rendelték: {max_amount}")