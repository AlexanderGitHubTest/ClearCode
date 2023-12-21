"""
Names to avoid.
"""

string - date_as_string
# Аргумент функции конвертации строковой даты в формат date.
# Было неинформативное и короткое имя.

float_num - number_float_format
# Аргумент функции форматирования чисел в формате с плавающей точкой в формат str для вывода в csv файл.
# Было неинформативное имя + префикс num даёт скрытый ненужный смысл.

number_row - phone_number_row_id
# "Многоусловный" if (фактически select case в форме elif elif elif ...). Обработка xls файла. 
# На основе названий в заголовке (первая строка) вычисление, в каком столбце телефонные номера.
# Поставщики меняют формат файла без предупреждения %)
# Было неинформативное имя (number вместо phone_number) и добавлен постфикс. 

charge_row - charge_row_id
# Аналогично предыдущей ситуации. Только вычисляем в каком столбце начисления.
# Добавлен постфикс.

result_file_query - output_file_name
# Функции передаётся запрос на выборку, имя файла, путь к файлу и имя листа Excel.
# Она сохраняет результат запроса в файл excel.
# Было неинформативное и не отображающее смысл имя переменной.

list_name - sheet_name
# Та же функция, что и в предыдущем пункте.
# Было использовано стандартное имя и не соответствующее .
# предметной области. Лист в excel - sheet.

len_period_names - num_periods
# Периоды, за которые выводится отчет, находятся в таблице.
# Много раз организуется цикл по ним (достаточно знать первый период и их количество).
# Чтобы не обращаться постоянно к базе данных, сохраняем количество периодов в переменную.
# Было использовано стандартное имя len и оно было вначале. Плюс точнее названа переменная. 

col - column_id
# Перебор по столбцам в таблице excel - переменная цикла.
# Было имя неполное и без постфикса.

value - value_cell
# Значение, которое будет занесено в ячейку excel.
# Было неинформативное имя.

max_row - row_id_max
# Максимальный номер столбца в таблице excel.
# Добавлен постфикс id, а постфикс max перенесен на нужное место.

dict1 - blocked_customer_ctn
dict2 - blocked_technical_ctn
# Переменные сохраняют словари соответственно по клиентским и по техническим блокированным телефонным номерам.
# Было использование цифр в имени, а также неинформативные имена.  

index_of_found - found_element_id
# Множества. Функция удаления по значению. Найденное значение индекса элемента, который нужно будет удалить.
# Конкретизировал, что именно найдено, и перенес постфикс на место.