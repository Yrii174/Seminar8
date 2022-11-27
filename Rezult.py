import stud as si
import cabin as cab


def option():
    print("\nЭто программа мониторинга обучения студентов")
    ch = int(input('Что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место студента \n \
    3: Выход\n \
    Вы выбрали: '))

    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in si.stbaza['Фамилия']:
            index = si.stbaza['Фамилия'].index(Surn)
        print(f"{si.stbaza['ID'][index]}, {si.stbaza['Имя'][index]},{si.stbaza['Фамилия'][index]}\n,{si.stbaza['Дата рождения'][index]}, {si.stbaza['Успеваемость'][index]}")
        print('\nвыполнить какую-то другую операцию - Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID студента: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" Место в классе - {cab.class_card['Предмет'][index]}\n\, за партой номер - {cab.class_card['Номер парты'][index]}, это {cab.class_card['Ряд'][index]}, парта - {cab.class_card['Вид парты'][index]}, Имя: {si.stbaza['Имя'][index]}, Фамилия - {si.stbaza['Фамилия'][index]}, и успеваемасть у студента: {si.stbaza['Успеваемость'][index]}")
            print('\nвыполнить другую операцию - Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('повторим')
    exit()

option()