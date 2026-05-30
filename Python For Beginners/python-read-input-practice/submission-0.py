def add_two_numbers() -> int:
    line = input()
    numbers = line.split(",")
    
    sum = int(numbers[0]) + int(numbers[1])

    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
