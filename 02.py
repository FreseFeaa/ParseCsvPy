import csv
import os
 
 
os.system("cls")

def parse_csv_file(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            data.append(row)
    return data

def filtered_books(books_list, keyword):
    filtered_books_list = []
    for book in books_list:
        if keyword.lower() in book[1].lower():
            filtered_books_list.append(book)
    return filtered_books_list

# Парсинг CSV файла
file_path = 'books2.csv'
books_data = parse_csv_file(file_path)

def longStick():
    print ('___________________________________________________________________________________________')
# Выбор книг с указанным параметром в названии
longStick()
def inputuser ():
    inp = input("Введите что-то для поиска:  ")
    return inp

filtered_books_list = filtered_books(books_data, inputuser())

# Вывод отфильтрованного списка книг
for book in filtered_books_list:
    print(book)

longStick()
print ('      Книга           Цена                      ( Цена расчитывется за все книги в наличии)')
def calculate_cost_per_book(filtered_books_list):
    cost_per_book_list = []
    for book in filtered_books_list:
        isbn = book[0]
        quantity = int(book[2])
        price = float(book[3])
        total_cost = quantity * price
        cost_per_book_list.append((isbn, round(total_cost, 2)))
    return cost_per_book_list

# Получение списка кортежей с расчетом общей стоимости каждой книги
cost_per_book_result = calculate_cost_per_book(filtered_books_list)

# Вывод списка кортежей с общей стоимостью каждой книги
for item in cost_per_book_result:
    print(item)

longStick()