
numbers: set[int] = {1, 2, 3, 4, 5}

even_numbers = set(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

square = set(map(lambda x: x ** 2, numbers))
print(square)

square_comp = {x: x ** 2 for x in numbers}

