"""
Class names.
"""

# Пункт 3.1. Улучшите пять имён классов в вашем коде.
# Обнаружил, что в своём коде классы совсем не создаю
# (исключение - классы для таблиц для SQLAlchemy).
# Поэтому взял программу парсинга pdf (без классов) и
# сделал названия классов, как если бы я хотел сделать её в ООП варианте,
# соответственно, получился формат <название существующей функции или переменной> - <название нового класса>.

f - PdfFile
# Класс - файл целиком в формате pdf.

pdfrw_read - PageOfFile
# Класс - страница файла.

stream_decoding - ObjectOfPage
# Класс - объект со страницы (страница содержит много объектов).

stream_decoding - TextOfObject
# Класс - отдельный текст из объекта
# Функция stream_decoding сразу и выделяет объекты и 
# после декодирования выделяет из них тексты.

agprior_searching - RowWithPattern
# Класс - строка таблицы, в которой содержится нужный шаблон.


# Пункт 3.2. Улучшите семь имён методов и объектов по схеме из пункта 2.
# Так как своего такого кода для анализа нет, просто придумал примеры.

set_input_file_name - set_file_name
set_output_file_name - set_file_name
# Класс InputFile - было имя метода set_input_file_name.
# Класс ResultFile - было имя метода set_output_file_name.
# Сделал единое имя методов.

get_result_of_query - calculate_cell_value
get_result_of_calculate - calculate_cell_value
# Класс ExecuteQuery - было имя метода get_result_of_query.
# Класс CalculateValue - было имя метода get_result_of_calculate.
# Оба класса рассчитывают значение для очередной ячейки excel.

process_catalog - process_item
process_page - process_item
process_object - process_item
# Класс PdfFile - было имя метода process_catalog.
# Класс PageOfFile - было имя метода process_page.
# Класс ObjectOfPage - было имя метода process_object.
# Все методы работают "конвейером", поэтому сделал единое имя методов.

click_button_yesno - click_button
click_button_return - click_button
# Класс ButtonYesNo - было имя метода click_button_yesno.
# Класс ButtonReturn - было имя метода click_button_return.
# Сделал единое имя метода для однотипных классов.

print_extended_view_of_config - repr_extended
print_extended_view_of_controller - repr_extended
# Класс Config - было имя метода print_extended_view_of_config.
# Класс Controller - было имя метода print_extended_view_of_controller.
# По сути эти методы - просто расширенная печать сведений об объекте,
# поэтому заменил на "расширенный repr".

ManagingDB - ControllerDB
ControllingGUI - ControllerGUI
# Класс ManagingDB - по сути контроллер для действий с базой данных.
# Класс ControllingGUI - контроллер для работы с выводом на экран.
# Поэтому сделал в названии общую часть Controller.

config_read - perform_initialization
setting_values - perform_initialization
# Класс QueryExecutor - для инициализации был метод config_read.
# Класс FileProcessor - для инициализации был метод setting_values.
# По сути оба метода - это инициализация, поэтому сделал общее название.
