'''
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

"""
Задача №38
реализовать копирование данных из файла А в файл B.
написать отдельную функцию copy_data:
прочитать список словарей (read_file)
и записать его в новый файл используя функцию standart_write
дополнить функцию main
"""

'''


from csv import DictReader, DictWriter
from os.path import exists


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            second_name = input('Введите фамилию:')
            if len(second_name) < 4:
                raise NameError('Слишком короткая фамилия')
            phone_number = input('Введите номер телефон:')
            if len(phone_number) < 11:
                raise NameError('Слишком короткий номер телефона:')
        except NameError as err:
            print(err)
        else:
            flag = True

    return [first_name, second_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=[
                         'first_name', 'second_name', 'phone_number'])
        f_w.writeheader()


def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {
        'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def remove_row(file_name):
    search = int(input("Введите номер строки для удаления: "))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search-1)
        standart_write(file_name, res)
    else:
        print('Введен неверный номер строки')


def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)

def search_record(file_name):
    if not exists(file_name):
        print(f"Файл {file_name} отсутствует")
        return

    characteristic = input("Введите имя или фамилию для поиска: ")
    records = read_file(file_name)
    found = [record for record in records if characteristic in record.values()]
    
    if found:
        for record in found:
            print(record)
    else:
        print("Запись не найдена")

file_name = "phone.csv"
file_name_new = "phone_new.csv"

def copy_data(file_name, file_name_new):
    if not exists(file_name):
        print(f"Исходный файл {file_name} отсутствует")
        return
    if not exists(file_name_new):
        create_file(file_name_new)
    data = read_file(file_name)
    standart_write(file_name_new, data)
    print(f"Данные скопированы из {file_name} в {file_name_new}")

def main():
    while True:
        command = input('Введите команду:')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print("Файла отсутствует, пожалуйста создайте файл")
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print("файл отсутствует")
            remove_row(file_name)
        elif command == "s":
            search_record(file_name)
        elif command == 'c':            
            copy_data(file_name, file_name_new)
        elif command == 'rn':
            if not exists(file_name_new):
                print('файл отсутствует, пожалуйста сначала скопируйте данные')
                continue
            print(*read_file(file_name_new))             
        elif command == 'help':
            print('Список команд: w - запись, r - чтение, d - удаление, s - поиск по имени или фамилии, c - копирование в file_name_new, rn - чтение из file_name_new, q - выход')                


main()
