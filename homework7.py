from datetime import datetime

date_str = input("Введіть дату (рррр-мм-дд): ")

target_date = datetime.strptime(date_str, "%Y-%m-%d")

today = datetime.now()

difference = target_date - today

print("До заданої дати залишилося", difference.days, "днів.")