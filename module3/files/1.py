# для работы c файлами есть стандартная функция open()
# пример использования
myfile = open("hello.txt", "w") # второй парамерт определяет в каком режиме открыт файл. w - write(запись), r - read(чтение)

	
myfile = open("image.png", "rb") # rb - режим чтения бинарного файла. не путать с тектовыми файлами которые можно прочитить даже обычным блокнотом
# a - означает запись в конец файла. то есть без перезаписи содержимого
# после работы с файлом, необходимо его закрыть программно. то есть удалить из памяти дискриптор и завершить процесс
myfile.close()


# так как работа с файлами не гарантирует безошибочной работы программы, необходимо использовать обработку исключений

try:
    myfile = open("hello.txt", "w")
    try:
        print("Работа с файлом")
    finally:
        myfile.close()
except Exception as ex:
    print(ex) # в этом блоке произойдет вывод ошибки ex
    # ниже представлены уточнение возможной ошибки
except FileExistsError as fe:
    print("файл не существует")
except PermissionError as pe:
    print("нет прав доступа к файлу")


# так же удобно работать с файлами через область видимости. with

with open("hello.txt", "w") as myfile:
    print("Работа с файлом myfile")

# эта конструкция позволяет программе самостаятельно освобождать дескриптор файла. но все еще требует обработку исключений

# пример записи в файл
with open("hello.txt", "w") as file:
    file.write("hello world") # write() записывает по строчно
    
print("Файл записан")

# так же можно записать массив строк черех writelines()
lines = ["Hello Word", "Hello Work", "Hello World"]
with open("hello2.txt", "a") as file:
    file.writelines(lines)
     
print("Список строк записан в файл")



# пример чтения из файла
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="") # построчный вывод


file.seek(2) # перемещаемся к нужному биту в файле. не всегда нужно


# полный пример работы с файлом

# имя файла
FILENAME = "messages.txt"
 
# запись строки в файл
def write():
    message = input("Введите строку: ")
    with open(FILENAME, "a") as file:
        file.write(message + "\n")
 
# чтение файла файл
def read():
    with open(FILENAME, "r") as file:
        for message in file:
            print(message, end="")
    print() # перевод строки для разделения меню и вывода
             
while(True):
    selection = int(input("1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: "))
    match selection:
        case 1: write()
        case 2: read()
        case 3: break
        case _: print("Некорректный ввод")
     
print("Программа завершена")



# полный пример работы с файлами csv - упрощенный таблицы данных

import csv # необходимо подключить библиотеку
 
FILENAME = "users2.csv"
 
users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]
 
with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    # по умолчанию ячейки разделены запятой
    # запись нескольких строк
    writer.writerows(users)
     
    user = {"name" : "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user) 
 
with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])