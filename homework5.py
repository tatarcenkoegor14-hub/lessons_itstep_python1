print("Привіт світ!")




def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


# приклад використання
nums = [10, 20, 30, 40, 50]
result = average(nums)

print("Середнє арифметичне:", result)