print(type(5)) # int class

print(type("John Doe")) # str class

class Client:
    def __init__(self, name, year_of_birth ):
        self.name = name
        self.year_of_birth = year_of_birth
    
    def get_name(self):
        return self.name

    def get_year_of_birth(self):
        return self.year_of_birth

    def set_name(self, new_name):
        self.name = new_name
    
    def calculate_age(self, actual_year):
        return actual_year - self.year_of_birth

john = Client ("John Doe", 1970) # példányosítás # john nevű véltozó a stacken van és a heapen lévő "john Doe"ra mutat

print(john.get_name())

jack = Client ("Jack Doe", 1980)

jack.set_name("Jack Smith")
print(jack.get_name())

print(jack.calculate_age(2022))
