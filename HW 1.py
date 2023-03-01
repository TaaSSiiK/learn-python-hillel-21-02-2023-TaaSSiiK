"""
Написати програму, яка конвертує радіани у градуси.
180 градусів - це Pi радіан.
Взідні дані:
радіани.
На виході:
конвертована величина градуси округлена до 5 цифр після коми
"""

# Додаємо бібліотеку для того щоб використовувати число пі
import math

# Питаємо у користувача вводні данні
rad = float(input('Введіть кількість радіан для конвектування у градуси'))

# Формула розрахунку
grad = rad * 180 / math.pi

# Даємо відповідь користувачу
print(f'{rad} радіан - це {round(grad, 5)} градусів')

# Повторюємо задачу в зворотньому напрямку
grad = float(input('Введіть кількість градусів якщо бажаєте перевести їх у радіани'))

rad = grad * math.pi / 180

print(f'{grad} градусів - це {round(rad, 5)} радіан')
