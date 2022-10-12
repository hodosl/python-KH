from pickle import TRUE


def remove_all(list, search):
    "This function removes all occurances if search is in list."
    # result = list.copy # létrehoz egy új listát másolással

    while search in list:
        list.remove(search)
    return list

names = ["John Doe", "Jane Doe", "Jack Doe", "John Doe"]
remove_all(names, "John Doe")
print(names)


def sum_numbers(numbers):
    """
    Többsoros leírás a függvényhez
    """
    sum_of_numbers = 0
    for i in numbers:
        if i == int(i):
            sum_of_numbers += i
    print(sum_of_numbers)

sum_numbers([2,5,3.4,7.5])

def count_positive_numbers(numbers):
    poznumbers = 0
    for i in numbers:
        if i > 0:
            poznumbers += 1
    return poznumbers
    
numbers= (1, -2, 3, -7)
count_positive_numbers(numbers)

print(min(numbers))

def is_all_positive(numbers):
    poznumbers = 0
    for i in numbers:
        if i >= 0:
            poznumbers += 1
    if poznumbers == len(numbers):
        print("TRUE")
    else:
         print("FALSE")

numbers= (1, -2, 3, 7)
is_all_positive(numbers)

if __name__ =="__main__":
    print("csak ha direktben futtatom fut le, ha importálom akkor nem")
