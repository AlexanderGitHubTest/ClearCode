"""
Names of functions/methods.
"""

str_to_date - converts_to_date - конвертирует строку формата <YYYY_MM_DD> в дату в формате date.

query_to_xlsx - save_query_to_xlsx - сохраняет заданный запрос в файл.

add_months - months_later - возвращает дату, отстоящую на заданное число месяцев от полученной.

arpu_vk - calculate_arpu_vk - вычислить значение ARPU по Вымпелкому.

file_reading - read_binary_file - прочитать бинарный файл.

line_marking - select_stream-endstream_blocks_from_lines - выделить блоки stream-endstream из строк.

stream_decoding - декодирует поток и ищет границы текста в декодированном потоке.
# так как два действия, разбил на две функции.
stream_decoding - decodes_stream - декодирует поток.
stream_decoding - searches_text_boundaries - ищет границы текста в декодированном потоке.

agprior_searching - searches_agprior_strings - ищет строки со словами "ПриорОбслАгент".

deque_palindrome - is_phrase_a_palindrome - определить, является ли фраза палиндромом.

queue_rotate - rotate_queue_in_a_circle - вращать очередь по кругу на N элементов.

button - process_button_clicks - обработка нажатия кнопок (в telegram боте).

in_which_constellation_is_the_planet - выводит в каком созвездии сегодня планета (в telegram боте).
# Разбил на три Функции, так как три действия: запрос планеты у пользвателя, расчёт названия созвездия и вывод названия созвездия.
in_which_constellation_is_the_planet - request_name_of_planet - запросить название планеты.
in_which_constellation_is_the_planet - calculate_name_of_constellation - рассчитать название созвездия.
in_which_constellation_is_the_planet - print_name_of_constellation - вывести название созвездия.
