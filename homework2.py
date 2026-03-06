a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))

# Введення математичної дії
operation = input("Введіть дію (+, -, *, /): ")

# Виконання обчислення
if operation == "+":
    result = a + b
    print("Результат:", result)

elif operation == "-":
    result = a - b
    print("Результат:", result)

elif operation == "*":
    result = a * b
    print("Результат:", result)

elif operation == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        result = a / b
        print("Результат:", result)

else:
    print("Невідома операція")