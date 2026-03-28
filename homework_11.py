text = "Це Приклад тексту З Деякими Словами"

words = text.split()
capital_words = [word for word in words if word[0].isupper()]

print(capital_words)