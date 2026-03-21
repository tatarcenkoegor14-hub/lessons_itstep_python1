import re

text = "Ось приклад: (123), ще число (456), і (7890)"

# шукаємо числа в дужках
numbers = re.findall(r"\((\d+)\)", text)

print("Знайдені числа:", numbers)
