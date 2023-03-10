"""
Написати програму, що проводить невеличкий діалог з користувачем:

Користувач вводить строку
Програма переводить строку в нижній регістр
Програма видаляє зі строки такі символи пунктуації: .,-:;?!()
Програма видаляє зайві пробіли / табуляції з правого кінця строки
Програма питає користувача яке слово (або словосполучення) він бажає замінити
Програма повідомляє на якому індексі строки словосполучення присутнє
Програма питає на яке слово треба замінити
Програма виводить відформатовану строку
Приклад роботи програми:

Please, input your string:
> HelLo, mY nAmE iS KyRyLo! I aM PrograMMing on C++) WhAt abOuT yoU? :)
What do you want to replace?
> C++
"C++" was found at position 46!
With what do you want to replace?
> Python
Here is your result:
hello my name is kyrylo i am programming on python what about you
"""
"""
Так як я здаю д/з вже після наступного уроку, то вирішив ускладнити собі завдання
Говорю відразу що вийшло у мене не ідеально, і це можна виправити
Але я й так витратив на все це багато часу
+ мені ліньки (адже тут є все що я хотів використати)
Помилку знайшов і показав
І грошей мені ніхто за цей проект не заплатить)))
Так що воно залишиться у такому вигляді)))
"""

# Вхідний текст
strfi = input('Доброго дня, введіть будь ласка ваш текст')

# Змінна для циклу всієї програми
choicetest = 0

# Сам цикл для всієї програми
while choicetest == 0:
    # Пуста змінна, цикл з "isinstance" та цикл з "or" зроблені для того, щоб був строгий перелік вибору
    # Ця схема повториться ще багато разів)
    choice = ''
    while not isinstance(choice, float):
        try:
            choice = float(input('''У який регістр ви бажаєте перевести ваш текст?
                             0 - нЕ пЕрЕвОдИтИ
                             1 - усі букви маленькі
                             2 - УСІ БУКВИ ВЕЛИКІ
                             3 - Перші Букви Слів Великі
                             4 - Тільки перша буква строки велика'''))
        except Exception:
            print('Ви зробили не зрозумілий вибір')
    while choice < 0 or choice > 4:
        print('Ви зробили не зрозумілий вибір')
        choice = ''
        while not isinstance(choice, float):
            try:
                choice = float(input('''У який регістр ви бажаєте перевести ваш текст?
                                 0 - нЕ пЕрЕвОдИтИ
                                 1 - усі букви маленькі
                                 2 - УСІ БУКВИ ВЕЛИКІ
                                 3 - Перші Букви Слів Великі
                                 4 - Тільки перша буква строки велика'''))
            except Exception:
                print('Ви зробили не зрозумілий вибір')

    # Завдяки "if" можемо вибрати регістр строки
    # Змінна "size" - це костиль який потрібен в кінці (ще повернемося)
    if choice == 4:
        strf = strfi.capitalize()
        size = 4
    elif choice == 3:
        strf = strfi.title()
        size = 3
    elif choice == 2:
        strf = strfi.upper()
        size = 2
    elif choice == 1:
        strf = strfi.lower()
        size = 1
    else:
        strf = strfi
        size = 0

    # Знову суровий вибір
    choice = ''
    while not isinstance(choice, float):
        try:
            choice = float(input('''Тепер виберіть чи бажаете ви прибрати абзаци, знаки пунктуації та табуляції?
                         0 - Нехай залишаються)
                         1 - Прибрати тільки зліва від тексту
                         2 - Прибрати тільки справа від тексту
                         3 - Прибрати по всьому тексту'''))
        except Exception:
            print('Ви зробили не зрозумілий вибір')
    while choice < 0 or choice > 3:
        print('Ви зробили не зрозумілий вибір')
        choice = ''
        while not isinstance(choice, float):
            try:
                choice = float(input('''Тепер виберіть чи бажаете ви прибрати абзаци, знаки пунктуації та табуляції?
                         0 - Нехай залишаються)
                         1 - Прибрати тільки зліва від тексту
                         2 - Прибрати тільки справа від тексту
                         3 - Прибрати по всьому тексту'''))
            except Exception:
                print('Ви зробили не зрозумілий вибір')

    if choice == 3:
        # І знову)
        choice = ''
        while not isinstance(choice, float):
            try:
                choice = float(input('''Ви бажаєте прибрати усі абзаци, знаки пунктуації та табуляції?
                                     0 - Ні, тільки по краях тексту
                                     1 - Так, бажаю прибрати все!
                                     2 - Бажаю прибрати тільки абзаци
                                     3 - Бажаю прибрати тільки табуляції
                                     4 - Бажаю прибрати тільки знаки пунктуації (.,-:;?!()'''))
            except Exception:
                print('Ви зробили не зрозумілий вибір')
        while choice < 0 or choice > 4:
            print('Ви зробили не зрозумілий вибір')
            choice = ''
            while not isinstance(choice, float):
                try:
                    choice = float(input('''Ви бажаєте прибрати усі абзаци, знаки пунктуації та табуляції?
                                         0 - Ні, тільки по краях тексту
                                         1 - Так, бажаю прибрати все!
                                         2 - Бажаю прибрати тільки абзаци
                                         3 - Бажаю прибрати тільки табуляції
                                         4 - Бажаю прибрати тільки знаки пунктуації (.,-:;?!()'''))
                except Exception:
                    print('Ви зробили не зрозумілий вибір')
        # Як жаль що ".replace" потребує написання кожного символу окремо((
        # Але тепер я це знаю))))
        if choice == 4:
            strf = strf.replace('.', '')
            strf = strf.replace(',', '')
            strf = strf.replace('-', '')
            strf = strf.replace(':', '')
            strf = strf.replace(';', '')
            strf = strf.replace('?', '')
            strf = strf.replace('!', '')
            strf = strf.replace('(', '')
            strf = strf.replace(')', '')
        elif choice == 3:
            strf = strf.replace('\t', '')
        elif choice == 2:
            strf = strf.replace('\n', '')
        elif choice == 1:
            strf = strf.replace('.', '')
            strf = strf.replace(',', '')
            strf = strf.replace('-', '')
            strf = strf.replace(':', '')
            strf = strf.replace(';', '')
            strf = strf.replace('?', '')
            strf = strf.replace('!', '')
            strf = strf.replace('(', '')
            strf = strf.replace(')', '')
            strf = strf.replace('\t', '')
            strf = strf.replace('\n', '')
        else:
            strf = strf.strip('.,-:;?!()\t\n ')
    elif choice == 2:
        strf = strf.rstrip()
    elif choice == 1:
        strf = strf.lstrip()

    # І знов те саме) Насправді мені здається що цей код складається тільки з "while" (він буде мені снитися)
    choice = ''
    while not isinstance(choice, float):
        try:
            choice = float(input('''Якщо ви бажаєте замінити якесь слово натисніть 1, якщо ні - 0'''))
        except Exception:
            print('Ви зробили не зрозумілий вибір')
    while choice < 0 or choice > 1:
        print('Ви зробили не зрозумілий вибір')
        choice = ''
        while not isinstance(choice, float):
            try:
                choice = float(input('''Якщо ви бажаєте замінити якесь слово натисніть 1, якщо ні - 0'''))
            except Exception:
                print('Ви зробили не зрозумілий вибір')
    # І ось ми дійшли до найцікавішого - до помилки!
    if choice == 1:
        word = input('Яке слово ви бажаєте замінити?')
        # Ось на цьому етапі я зрозумів що регістр має дуже велике значення коли не знайшов слово яке є)
        # Тому я змінив регістр розшукуваного слова та запам'ятав строку яка в мене вже була на цьому етапі
        word = word.lower()
        # Назву цієї змінної я поясню нижче
        strerror = strf
        strf = strf.lower()
        # "Мне за эту разработку такую премию дадут")))
        # Я шукаю індекс та зберігаю його як змінну
        # Для того, щоб запустити цикл, та знайти не тільки перше слово, а всі слова у рядку
        index = strf.find(f'{word}')
        # Ця змінна для того, щоб якщо цикл не запустився нам вискочив "print" який скаже що не знайшов потрібне слово
        prost = 0
        while not index == -1:
            print(f'Ваше слово знайдене під індексом {index}')
            prost = prost + 1
            index = strf.find(f'{word}', index + 1)
            neword = input('На що ви бажаєте замінити знайдене слово?')
            strf = strf.replace(f'{word}', f'{neword}')
            # Змінна "size" існує для того, щоб запам'ятати вибір користувача та повернути регістр після заміни слова
            if size == 4:
                strf = strf.capitalize()
            elif size == 3:
                strf = strf.title()
            elif size == 2:
                strf = strf.upper()
            elif size == 1:
                strf = strf.lower()
            # Насправді треба шукати цю помилку, бо навряд чи хтось захоче писати спеціально різним регістром,
            # та ще й зберегти це, але після ≈ 1000000 спроб знайти помилки в коді я її знайшов
            # і поки що не знаю як її обійти, але я впевнений що все ще попереду і не треба бігти поперед батька...
            else:
                print('''Я визнаю свою помилку!
Я не можу замінити слово у якого невідомо який регістр попереду, так щоб його (регістр) не змінити
Тому я повертаю відформатований текст але без заміни слова(((''', f'\n{strerror}', '\nВибач(')
                exit()
        if prost == 0:
            print('Ваше слово не знайдено')
    # Ось нарешті ми дійшли до відформатованого тексту, я вважаю це перемогою))))
    print(strf)
    # Але перемога то не кінець))) тому програма пропонує перемогти ще раз і ще раз)
    choicetest = ''
    while not isinstance(choicetest, float):
        try:
            choicetest = float(input('''Ви бажаєте змінити форматування вашого тексту?
                            0 - Так
                            1 - Ні'''))
        except Exception:
            print('Ви зробили не зрозумілий вибір')
    while choicetest < 0 or choice > 1:
        print('Ви зробили не зрозумілий вибір')
        choicetest = ''
        while not isinstance(choice, float):
            try:
                choicetest = float(input('''Ви бажаєте змінити форматування вашого тексту?
                                0 - Так
                                1 - Ні'''))
            except Exception:
                print('Ви зробили не зрозумілий вибір')
# На справді мені здається що тут і так все зрозуміло без моїх коментарів,
# Але я розумію їх значення тому не проти їх написати
# Пробачте якщо вони не дуже інформативні, але краще я поки зробити не можу)
print('Гарного дня, до побачення ;)')

# До речі помилку "Too broad exception clause" за помилку не вважаю, якщо ви вважаєте, то можемо вступити у діскусію)
