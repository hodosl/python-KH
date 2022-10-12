# adjuk össze az első egymillió számot
# sum() függvénnyel # iterable vagyis bejárhatóak a paraméterei

def firstn(n):
    num = 0
    while num < n:
        yield num  # csak az aktuális sorozat elemet állítja elő és visszaadja
        num += 1


numbers = []
i = 0
while i < 1_000_000:
    numbers.append(i)
    i += 1

print(sum(numbers))

print([i for i in firstn(10)]) # csak az aktuális sorozat elemet állítja elő, nem az egész sorozatot

def fibonacci(limit):
    yield 1
    yield 1
    first = 1
    second = 2
    while first < limit:
        result = first + second
        yield result
        first = second
        second = result
        