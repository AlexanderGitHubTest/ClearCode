"""
Variable names 2.
"""



# Пункт 6.1. Разберите свой код, и сделайте пять примеров, где можно более наглядно учесть в именах переменных уровни абстракции.
# Исходный код из программы парсинга pdf.
# Программа считывает из папки pdf файлы (по сути счета, по внутреннему виду - таблицы),
# ищет в них данные двух категорий и каждую категорию записывает в отдельный файл в формате csv.
# В данной программе выделил следующие уровни абстракции:
# - чтение папки с исходными файлами - запись результатов;
# - чтение одного файла;
# - декодирование объектов, находящихся на странице;
# - поиск необходимого в декодированном.


# Пример 1. Чтение папки с исходными файлами - запись результатов.

fields - AGPRIOR_HEADER_FIELDS
# Константа: Список полей (list) для "шапки" результирующего csv файла по категории AGPRIOR

FILE_NAME_AGPRIOR - AGPRIOR_FILE_NAME
# Константа: Имя (string) результирующего csv файла по категории AGPRIOR

fields_otc - OTC_HEADER_FIELDS
# Константа: Список полей (list) для "шапки" результирующего csv файла по категории ONE_TIME_CHARGE

FILE_NAME_ONE_TIME_CHARGE - OTC_FILE_NAME
# Константа: Имя (string) результирующего csv файла по категории ONE_TIME_CHARGE

list_of_pdf - list_of_source_files
# Список (glob) исходных файлов в формате pdf


# Пример 2. Чтение одного файла.

fdata - file_data
# Содержимое файла (string)

x - file_PdfReader
# Объект PdfReader с содержимым файла

x - file_page
# Одна страница из файла (перебор страниц в цикле for)

stream_line - file_page_content_encoding
# Содержимое ("content") страницы, преобразованное в байтовый формат (кодировка latin-1)


# Пример 3. Декодирование объектов, находящихся на странице.

stream_line - line_from_page
# Строка из содержимого страницы

stream_line_decode - line_from_page_decoding
# Декодированная (разархивированная) строка

pos_begin - position_beginning_text
# Позиция начала текста в строке

pos_end - position_beginning_text
# Позиция конца текста в строке (скобки после текста)

pos_double_slash - position_double-slash_in_text
# Позиция двойного слэша ("\\") в тексте


# Пример 4. Поиск необходимого в декодированном.

list_of_6_strings - table_row
# Строка таблицы (необходимая таблица имеет 6 столбцов)

onetime_charges - objects_otc_category_found
# Признак, что найдены объекты категории ONE_TIME_CHARGE

string - value_in_table_row
# значение в строке таблицы


# Пример 5. Есть отдельная программа, которая сводит в один файл в формате csv результаты работы программы,
# которая приведена в примерах 1 - 4.

sql_groupping_agprior - agprior_groupping
# Запрос SQL для группировки категории AGPRIOR

sql_groupping_onecharge = otc_groupping
# Запрос SQL для группировки категории ONE_TIME_CHARGE

sql_result = result_intersection
# Результирующий запрос SQL

row - agprior_groupping_row
row - otc_groupping_row
row - result_intersection_row
# Строка в запросах (для перебора строк)

sql_result_out - result_intersection_formatted
# Форматирующий запрос SQL для вывода в файл

tuple_for_out - output_row
# Строка форматирующего запроса SQL для вывода в файл (tuple)

dict_for_out - output_row_with_field_names
# Строка форматирующего запроса SQL для вывода в файл с добавленными названиями полей (dict)



# Пункт 6.2. Приведите четыре примера, где вы в качестве имён переменных использовали или могли бы использовать технические термины из информатики.

decoding_line - line_from_page_iterator
# Итератор декодированных строки из контента страницы

agprior_line - agprior_line_iterator
# Итератор строк по категории agprior

fields - AGPRIOR_HEADER_FIELDS_LIST
# Константа: список полей заголовка результирующего csv файла по категории agprior

addr - e-mail_address_sorted
# Почтовые адреса, отсортированные 



# Пункт 6.3. Придумайте или найдите в своём коде три примера, когда имена переменных даны с учётом контекста (функции, метода, класса).

# Пример 1.
def decode_contest_from_page (page):   
    size_of_upper_margin = ...
    contest_encoding = ...

# Пример 2.
class Auto:
    engine_power = ...
    body_type = ...

# Пример 3.
class Queue:
    def rotate_queue(direction, shift):
        rotate_metod = ...
        size_of_element = ...



# Пункт 6.4. Найдите пять имён переменных в своём коде, длины которых не укладываются в 8-20 символов, и исправьте, чтобы они укладывались в данный диапазон.

section - report_section
# Секция из списка секций для создания отчета (используется для перебора секций в цикле)

file_page_content_encoding - encoded_page_content
# Содержимое ("content") страницы, преобразованное в байтовый формат (кодировка latin-1)

output_row_with_field_names - out_row_fields_added
# Строка форматирующего запроса SQL для вывода в файл с добавленными названиями полей (dict)

index - slot_index
# Найденный индекс для операции put в ассоциативном массиве

lineobj - line_from_file
# строка из файла
