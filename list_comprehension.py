# Lista származtatása

numbers = [i for i in range(0, 5)]
print(numbers)


#ugyanaz mint előbb
numbers = []
for i in range(0, 5):
    numbers.append(i)

print(numbers)

numbers = [i ** 2 for i in range(0,5)] # számok négyzete
print(numbers)

names = ["John Doe", "Jack Doe"]
uppers =  [n.upper() for n in names]
print(uppers)

names = ["John Doe", "Jack Doe", "Bob"]
result = [len(n) for n in names]
print(result)

names = ["John Doe", "Jack Doe", "Bob"]
result = [n for n in names if "J" in n]
print(result)

numbers = [1,2,3,4,5,6]
result = [n for n in numbers if n % 2 == 0] # páros számok
print (result)

numbers = [1,2,3,4,5,6]
result = [n *2 for n in numbers if n % 2 == 0] # páros számok dupláját
print (result)

def get_all_positive_numbers(numbers):
    return [n for n in numbers if n> 0]

def double_values(numbers):
    return [n*2 for n in numbers]