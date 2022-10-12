def print_employee(name, year_of_birth):
    print("Name: " + name)
    print("Year of birth: " + str(year_of_birth))


print_employee("john Doe", 1980)

employee = ("John Doe", 1980)

print_employee(*employee)

print_employee(employee[0], employee[1]) #ez ugyanaz mint az előbb, csak a felső kibontja magától

employee = {"year_of_birth": 1982, "name": "Jane Doe"}
print_employee(**employee) # sorrenben csomagolja ki dictionaryből