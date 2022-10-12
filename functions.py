def print_name(name, count): # formális paraméterek
    for i in range(count):
        print(name)

print_name("John", 5) # sorrendi kötés # aktuális paraméterek #positional agument

print_name(count=5, name="Doe") # név szerinti kötés #keyword

def sum_numbers(*args): # több argumentum tupple be becsomagolva
    print(type(args))
    print(args)
    for number in args:
        print(number)


sum_numbers(1,2,3,4)

def print_parameters(**kwargs): # több argumentum dictionarybe becsomagolva
    print(type(kwargs))
    print(kwargs)

print_parameters(name="John", yob=1970)
