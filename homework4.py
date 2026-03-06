def count_vowels(*strings):
    vowels = "aeiouyAEIOUYаеєиіїоуАЕЄИІЇОУЮ"
    count = 0

    for s in strings:
        for char in s:
            if char in vowels:
                count += 1

    return count



result = count_vowels("Привіт", "Python", "Програмування")
print("Кількість голосних літер:", result)
