import pandas as pd

print('----'*40)
print('Табель учащихся в средней школе # 1285')

stbaza = {
        'ID': ['01','02','03','04','05'],
        'Имя' : ['Петр','Сергей','Екатерина','Ольга','Мария'],
        'Фамилия': ['Сидоров','Бойко','Литовченко','Мессинг','Пастернак'],
        'Дата рождения' : ['22.01.1999','04.05.2001','01.04.1999','23.02.2002','08.03.2004'],
        'Успеваемость' : ['Хорошист','Троечник','Хорошист','Отличник','Хорошист']
}
    
sc = pd.DataFrame(data = stbaza)

with open('students.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)
