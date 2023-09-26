import random as rnd
import time

print(
    """
    ___________ ___________   ____________________
    \__    ___/ \_   _____/  /   _____/\__    ___/
      |    |     |    __)_   \_____  \   |    |   
      |    |     |        \  /        \  |    |   
      |____|    /_______  / /_______  /  |____|   
                        \/          \/            

    Периодическая таблица Менделеева из первых 27 химических элементов
    
    
    Здесь есть несколько режимов:
    
    1. В тесте будут выбраны 10 случайных, на которые вы должны будете дать ответ на русском (регистр не важен)
    2. В тесте будет неограничееное кол-во вопросов, но с ограничением по времени в 10 секунд
    3. Бесконечный тест
    
    """
)

el = {
    "N": "азот",
    "Al": "алюминий",
    "Ba": "барий",
    "B": "бор",
    "H": "водород",
    "Fe": "железо",
    "Au": "золото",
    "I": "иод",
    "K": "калий",
    "Ca": "кальций",
    "O": "кислород",
    "Si": "кремний",
    "Mg": "магний",
    "Mn": "марганец",
    "Cu": "медь",
    "As": "мышьяк",
    "Na": "натрий",
    "Sn": "олово",
    "Hg": "ртуть",
    "Pb": "свинец",
    "S": "сера",
    "Ag": "серебро",
    "C": "углерод",
    "P": "фосфор",
    "F": "фтор",
    "Cl": "хлор",
    "Zn": "цинк"
}

keys = list(el.keys())

while True:
    choice = int(input("Выберите режим: "))
    rnd.shuffle(keys)

    if choice == 1:
        result = 0
        wrong_answered = {}

        for i in range(10):
            inp = input(f"Что такое {keys[i]}? ")
            if inp.casefold() == el[keys[i]].casefold():
                result += 1
            else:
                wrong_answered[keys[i]] = inp

        print(f"Ваш результат: {result / 10 * 100}% ({result} из 10)")

        if result != 10:
            print()
            print("Неправильные ответы: ")
            for key in wrong_answered.keys():
                print(f"{key} - {wrong_answered[key]} (Правильный ответ - {el[key]})")

    if choice == 2:
        result = 0
        wrong_answered = {}

        t0 = time.time()

        i = 0

        while time.time() - t0 < 10.0:
            if i >= 26:
                i = 0
                rnd.shuffle(keys)

            now = keys[i]
            inp = input(f"Что такое {now}? ")
            if inp.casefold() == el[now].casefold():
                result += 1
            else:
                wrong_answered[now] = inp

            i += 1

        print(f"Правильный ответов: {round(result / (result + len(wrong_answered)) * 100, 2)}% (Правильных ответов: {result}; "
              f"Неправильных ответов - {len(wrong_answered)})")

        if len(wrong_answered) > 0:
            print()
            print("Неправильные ответы: ")
            for key in wrong_answered.keys():
                print(f"{key} - {wrong_answered[key]} (Правильный ответ - {el[key]})")

    if choice == 3:
        result = 0
        print("Чтобы остановиться напишите \"выход\"")

        ans = ""

        i = 0

        while True:
            if i >= 26:
                i = 0
                rnd.shuffle(keys)

            now = keys[i]
            ans = input(f"Что такое {now}: ")

            if ans.casefold() == "выход".casefold():
                break

            if ans.casefold() == el[now].casefold():
                print("Правильно")
            else:
                print(f"Неправильно, правильный ответ - {el[now]}")

            i += 1

    print()