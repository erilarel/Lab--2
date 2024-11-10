from csv import reader


# Задание 1
count = 0
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1]) > 30:
            count +=1
print(count)


# Задание 2
while True:
    search = input('Введите имя автора на английском языке: ')
    if search == '0':
        break
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            if row[2].lower() == search.lower():
                if float(row[6].replace(',', '.')) > 150: #условие 6 варианта
                    print(row[1])
            else:
                print("Данного автора нет в нашей базе или его книги стоят меньше 150 рублей")
                break


# Задание 3
import random

output = open('result.txt', 'w')
obchii_spisok = []
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        obchii_spisok.append(row)
    for i in range(1, 21):
        k = random.randint(0, len(obchii_spisok))
        output.write(f'{i}) {obchii_spisok[k][2]}. {obchii_spisok[k][1]} - {obchii_spisok[k][3]}\n')

output.close()