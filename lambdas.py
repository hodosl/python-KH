def multiply(numbers):
    result = []
    for number in numbers:
        atomic_result = number * 2
        result.append(atomic_result)
    return result

def add_five(numbers):
    result = []
    for number in numbers:
        atomic_result = number +5
        result.append(atomic_result)
    return result

print(multiply([1,2,3,4,5]))

def apply(numbers, f): # egy utasítás, függvény a paraméter
    result = []
    for number in numbers:
        atomic_result = f(number)
        result.append(atomic_result)
    return result

def multiply(number):
    return number * 2
def add_five(number):
    return number + 5

print(apply([1,2,3,4,5], multiply ))
print(apply([1,2,3,4,5], add_five ))

print(apply([1,2,3,4,5], lambda n: n*3)) #egyszeri függvény n a paraméter--> : után a törzse


def print_names(transform):
    for i in range (0,10):
        print(transform("trainer"))

# def convert_to_upercase(s):
    # return s.upper()

# convert_to_uppercase = lambda s: s.upper()
#print_names(convert_to_upercase)
print_names(lambda s: s.lower())

#Lambda függvény gyártás

def make_incrementor(increment):
    return lambda number: number + increment

increment_with_42 = make_incrementor(42)

i=10
print(increment_with_42(i))


