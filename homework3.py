def square_list(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = square_list(nums)

print("Початковий список:", nums)
print("Список квадратів:", squared)


def square_list(numbers):
    result = []
    for n in numbers:
        result.append(n ** 3)
    return result



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = square_list(nums)

print("Початковий список:", nums)
print("Список кубів:", squared)