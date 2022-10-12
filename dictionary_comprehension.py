from pprint import pprint


numbers = {n:n**2 for n in range (1, 10) if n % 2== 0}

print(numbers)

pprint(numbers)
