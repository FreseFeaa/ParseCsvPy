import csv

def get_books(file_path):
    books_data = []
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='|')
        for row in csv_reader:
            books_data.append(row)
    
    return books_data

# Пример использования
file_path = "books.csv"
books_list = get_books(file_path)
print(books_list)

#Я сделал несколько файлов, ткк в books (Задание 1) разделитель везде "|""  , 
# а в задании 2 и 3, там после книги еще разделитель ",". Поэтому несколько файлов