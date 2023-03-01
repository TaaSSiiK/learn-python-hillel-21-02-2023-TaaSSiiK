"""
Написати програму, що рахує абонплату за комунальним лічильника (наприклад, електроенергії або газу).
Вхідні дані:
попередні показання
теперішні показання
тариф.
На виході:
скільки потрібно сплатити, округлено до двох цифр після коми
"""

tarif = 1.75
# Запитуємо у користувача вхідні данні
lastind = float(input(
    'Введідь ваші останні показання лічильника для того щоб порахувати скільки ви повинні заплатити в цьому мусяці'))

nowind = float(input('Тепер введіть теперешні показання лічильника'))

# Повідомляємо користувачу його тариф
print(f'Ваш тариф {tarif}грн/кВт')

# Формула розрахунку
sumgrn = (nowind - lastind) * tarif

# Повідомляємо користувачу результат розрахунку
print(f'Ви маєте сплатити {round(sumgrn, 2)}грн')
