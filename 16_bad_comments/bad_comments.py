Bad Comments.
"""

# правка 1
# БЫЛО
    # Добавлено для прохождения задания (2-я неделя, 4-я часть)
    dp.add_handler(CommandHandler("planet", in_which_constellation_is_the_planet))
# СТАЛО
    dp.add_handler(CommandHandler("planet", in_which_constellation_is_the_planet))
# КОММЕНТАРИЙ:
# "8. Слишком много информации" 
# - убрал подробности, не относящиеся к делу


# правка 2
# БЫЛО
def greet_user(update, bot):
    # ... код
    # присваиваем значение глобальной переменной
    chat_id = update.message.chat_id
# СТАЛО
def greet_user(update, bot):
    # ... код
# КОММЕНТАРИЙ:
# "2. Бормотание" и "3. Недостоверные комментарии"
# - комментарий невнятный: то ли используется глобальная переменная
# и ей присваивается значение (что неправда - переменная локальная),
# то ли мы используем глобальную переменную, что, опять же неверно,
# так как update было передано функции и это локальная переменная;
# в итоге переменная chat_id в функции не используется и комментарий удалён

# правка 3
# БЫЛО
    # список кнопок
    button_list = [
# СТАЛО
    buttons_list = [
# КОММЕНТАРИЙ:
# "7. Избыточные комментарии"
# - название переменной самодостаточно 
# (только для точности множественное число сделал)

# правка 4
# БЫЛО
# Обработка нажатия кнопок
def button(update, bot):
# СТАЛО
handle_tapping_buttons(update, bot):
    """
    Обработать нажатия кнопок.
    """
# КОММЕНТАРИЙ:
# "12. Не используйте комментарии там, где можно использовать функцию или переменную"
# - сделал правильное имя функции
# (комментарий оставил только как перевод на русский)

# правка 5
# БЫЛО
    # `CallbackQueries` требует ответа, даже если 
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы. 
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
# СТАЛО
    # нужно обязательно отправить ответ (даже пустой), чтобы выключить индикатор выполнения у пользователя
    # Подробнее: After the user presses a callback button, Telegram clients 
    # will display a progress bar until you call answerCallbackQuery. 
    # It is, therefore, necessary to react by calling answerCallbackQuery even if no notification 
    # to the user is needed (e.g., without specifying any of the optional parameters). 
    # Информация отсюда: https://core.telegram.org/bots/api#callbackquery.
    query.answer()
# КОММЕНТАРИЙ:
# "3. Недостоверные комментарии"
# - был некорректный комментарий

# правка 6
# БЫЛО
#        Закомментил вариант с редактированием текста вместо стирания:
#        query.edit_message_text(text="Можем позаниматься астрологией: поискать, в каком созвездии какая планета. Набери: /planet и название планеты по-английски с большой буквы (например, '/planet Mars').")
# СТАЛО
# КОММЕНТАРИЙ:
# "11. Закомментированный код"
# - удалил его

# правка 7
# БЫЛО
    #преобразуем строку в список
    text_list = update.message.text.split(" ")
# СТАЛО
    user_response_as_list = update.message.text.split(" ")
# КОММЕНТАРИЙ:
# "4. Шум"
# - убрал комментарий, не несущий информации
# - дополнительно переменной дал осмысленное имя

# правка 8
# БЫЛО
from datetime import date, datetime
# ... много кода
# Конвертирует строку в дату в формате date
def str_to_date(string):
    date_in_datetime = datetime.strptime(string,"%d.%m.%Y")
    return date(date_in_datetime.year, date_in_datetime.month, date_in_datetime.day)
# СТАЛО
from datetime import date, datetime
# ... много кода
def convert_str_to_date(string: str) -> date:
    # пример корректной исходной строки "15.12.2023"
    return datetime.strptime(string,"%d.%m.%Y").date()
# КОММЕНТАРИЙ:
# "4. Шум"
# - убрал комментарий, который можно заменить "правильным" именем функции
# - поменял имя функции и добавил аннотации типов
# - упростил код и добавил комментарий для наглядности использованного шаблона

# правка 9
# БЫЛО
# Дает полный путь к папке, где файл (без имени файла)
basedir = os.path.abspath(os.path.dirname(__file__))
# в эту папку будут выгружаться выводы запросов
# результат в RESULT_FILE, а подробности 
# в QUERY_OUTPUT_FILES_PATH
# файлы по периодам (yyyymm.xlsx), внутри вкладки по отчетам
# Имя вкладки - номер (типа 3.1.1.), в самой вкладке
# первой строкой полное название, далее сам отчет
QUERY_OUTPUT_FILES_PATH = "reports\\out\\"
OUTPUT_FILES_PATH = "reports\\" 
RESULT_FILE = "result.xlsx"
# СТАЛО
# Полный путь к каталогу, в которой находится эта программа python
# Внутри него находятся подкаталоги с исходными файлами данных
# и файлами результатов
basedir = os.path.abspath(os.path.dirname(__file__))
# Каталог внутри basedir, в котором находятся все исходные файлы и файлы результатов
WORKING_FILES_PATH = "reports\\" 
# Подкаталог с исходными файлами (внутри OUTPUT_FILES_PATH)
INPUT_FILES_PATH = "in\\" 
# Имя файла с результатами (внутри OUTPUT_FILES_PATH)
RESULT_FILE_NAME = "result.xlsx"
# Подкаталог c данными по периодам (внутри OUTPUT_FILES_PATH) - дополнение к файлу с результатами
RESULTING_FILES_BY_PERIOD_PATH = "out\\"
# КОММЕНТАРИЙ:
# "2. Бормотание" + "1. Неочевидные комментарии" + "9. Нелокальная информация"
# - комментарии был невнятные, исправил, чтобы было однозначно понятно
# - также переменная basedir комментировалась и до и после неё,
# что делало комментарии непонятными
# - INPUT_FILES_PATH объявлялся в другом месте, перенёс сюда
# - убрал подробное описание содержимого QUERY_OUTPUT_FILES_PATH (ему здесь не место)
# - в целом структурировал описание и переименовал константы для лучшего соответствия содержанию

# правка 10
# БЫЛО
# Инициализирую выгрузку в csv (AGPRIOR)
fields = ["phone", "from_date", "to_date", "service_name", "fee", "type"]
# ... много кода
# Инициализирую выгрузку в csv (ONE_TIME_CHARGE)
fields_otc = ["phone", "description", "charge", "quantity", "summa", "type"]
# ... много кода
# СТАЛО
AGPRIOR_CSV_HEADER_FIELDS = [ # ... содержимое константы
OTC_CSV_HEADER_FIELDS = [     # ... содержимое константы
FILE_NAME_AGPRIOR = "pdf\\agprior.csv"
FILE_NAME_OTC = "pdf\\onecharge.csv"
def download_from_csv_to_table(csv_header_fields, csv_file_name, session, class_table):
    """
    Загрузить все данные из csv файла в таблицу SQLAlchemy:
    - csv_header_fields - поля заголовка CSV файла
    - csv_file_name - полный путь + имя CSV файла
    - session - сессия SQLAlchemy
    - class_table - имя класса SQLAlchemy, куда будут загружены данные 
    """
    fields_list = [element["name"] for element in csv_header_fields]
    # ... много кода
download_from_csv_to_table(AGPRIOR_CSV_HEADER_FIELDS, FILE_NAME_AGPRIOR, session, Agprior)
download_from_csv_to_table(OTC_CSV_HEADER_FIELDS, FILE_NAME_OTC, session, OneCharge)
# КОММЕНТАРИЙ:
# "3. Недостоверные комментарии" + "9. Нелокальная информация"
# - комментарии были совсем неверные, в блоках ниже комментариев загрузка из csv,
# а не выгрузка в csv + комментарии относятся не к коду сразу за ними, а
# к целым программным блокам
# - эти два блока полностью переделаны, выделена функция и константы 
# и функция уже прокомментирована в целом

# правка 11
# БЫЛО
    # Попробую прочитать весь файл построчно
    with open(pdf_file, "rb") as f:
# СТАЛО
    with open(pdf_file, "rb") as f:
# КОММЕНТАРИЙ:
# "4. Шум"
# - комментарий не нужен, так как он просто дублирует понятный код

# правка 12
# БЫЛО
# Функция сохраняет заданный запрос в файл
# Получает:
# - query - сам запрос
# - file_path - путь к файлу
# - file_name - имя файла
# - list_title - заголовок листа в xlsx файле
# (это будет использовано первой строчкой листа,
# также начало заголовка до первого пробела будет
# использовано как название листа)
def save_query_to_xlsx(query, file_path, file_name, list_title):
    result_file_query = f"{file_path}{file_name}.xlsx"
    list_name = list_title[:list_title.find(" ")]
    # Если файл есть, используем его, если нет,
    # то создаем новый
    if os.path.isfile(result_file_query):
        file_exist = True
    else:
        file_exist = False
    if file_exist:
        wbq = load_workbook(result_file_query)
        wsq = wbq.create_sheet(list_name)
    else:
        wbq = Workbook()
        wsq = wbq.active
        wsq.title = list_name
    _ = wsq.cell(column=1, 
            row=1, 
            value=list_title)
    for row, query_string in enumerate(query):
        for col, query_string_value in enumerate(query_string):
            _ = wsq.cell(column=col+1, 
            row=row+2, 
            value=query_string_value)
    if file_exist:
        wbq.save(filename = result_file_query)
    else:
        wbq.save(filename = result_file_query)
# СТАЛО
def save_query_to_xlsx(query, file_path, file_name, section_id):
    """    
    Сохранить заданный запрос в файл в формате xlsx.
    Получает:
    query - сам запрос
    file_path - путь к файлу
    file_name - имя файла
    section_id - уникальное название секции
    """
    # часть названия секции до первого пробела будет использована как название листа excel
    list_name = section_id[:section_id.find(" ")]
    # если файл есть, используем его, если нет, то создаем новый
    if os.path.isfile(f"{file_path}{file_name}.xlsx"):
        wbq = load_workbook(result_file_query)
        wsq = wbq.create_sheet(list_name)
    else:
        wbq = Workbook()
        wsq = wbq.active
        wsq.title = list_name
    # название секции выгружаем как первую строку листа
    _ = wsq.cell(column=1, 
            row=1, 
            value=section_id)
    # выгружаем остальные строки из переданного запроса
    for row, query_string in enumerate(query):
        for col, query_string_value in enumerate(query_string):
            _ = wsq.cell(column=col+1, 
            row=row+2, 
            value=query_string_value)
    wbq.save(filename = f"{file_path}{file_name}.xlsx")
# КОММЕНТАРИЙ:
# "9. Нелокальная информация"
# - перенёс комментарий касательно использования list_title
# из описания функции непосредственно в место использования
# внутри функции
# - убрал лишнее из функции

# правка 13
# БЫЛО
    # Выведем в excel названия периодов
    period_names = session.query(InitialData).all()
    # Сделаю отдельную переменную, чтобы каждый раз не считать
    len_period_names = len(period_names)
    # ... код
            for col in range(len_period_names - 
                (lambda last_period: 0 if last_period else 1)(
                section["output_the_last_period"])):
                # ... код
                        value=section["function_name"](period_names[col].period_name))
                        # ... код               
                                            str(period_names[col].period_name)[:7], 
    # ... код
    for col in range(len_period_names):
# СТАЛО
   # Список названий периодов
   period_names = [period[0].isoformat() 
                   for period 
                   in session.query(InitialData.period_name).all()
                  ]
    # ... код
            for col in range(len(period_names) - 
                (lambda last_period: 0 if last_period else 1)(
                section["output_the_last_period"])):
                # ... код
                        value=section["function_name"](period_names[col]))
                        # ... код               
                                            str(period_names[col][:7], 
    # ... код
    for col in range(len(period_names)):
# КОММЕНТАРИЙ:
# "3. Недостоверные комментарии" + "1. Неочевидные комментарии"
# - комментарий и непонятен (к чему относится: к следующей строке или к блоку текста)
# и некорректен (в переменную считываются не названия периодов, а вся таблица InitialData)
# - исправлен сам комментарий и теперь в переменной действительно список названий периодов
# - убрана переменная len_period_names вместе с комментарием
# - упрощен код обращения к period_names, так как не нужно получать .period_name

# правка 14
# БЫЛО
    # Установим правильное форматирование ячеек строки названий периодов
    for col in range(len(period_names)):
        # форматирование строки периодов
        ws[
            f"{utils.cell.get_column_letter(col+2)}{1}"
        ].number_format = "mmmm yyyy;@"
# СТАЛО
    # установим правильное форматирование ячеек строки названий периодов
    for column in range(len(period_names)):
        # пример полученного формата: "Декабрь 2023"
        ws[f"{utils.cell.get_column_letter(column+2)}{1}"
          ].number_format = "mmmm yyyy;@"
# КОММЕНТАРИЙ:
# "4. Шум"
# - вместо бессмысленного комментария привел пример полученного формата

# правка 15
# БЫЛО
    # бывают разные названия листов, поэтому просто использую первый лист
    ws = wb[wb.sheetnames[0]]
    # Из файла считываем 2 столбца:
    # 1) Номер телефона. Всегда в столбце A
    # 2) Сумма начислений - варианты вычисляются в зависимости от заголовка
    # Всегда первая строка заголовок, вторая строка и далее данные 
    # Иногда бывает строка с подсчетом общей суммы
    # Чтобы ее не считывать, будем проверять, что номер телефона - число
    for i, row in enumerate(ws.rows):
        if i == 0:
            # вычисляем номера столбцов для начислений
            if row[2].value == "score_sum": # столбец С
                charge_row = 2
            elif row[2].value == "Сумма списаний": # столбец С
                charge_row = 2
            elif row[3].value == "Общий итог": # столбец E
                charge_row = 3
            elif row[4].value == "Общий итог": # столбец E
                charge_row = 4
            elif row[6].value == "Общий итог": # столбец G
                charge_row = 6
            else:
                raise "Ошибочный формат файла с начислениями по авансовым!"
            continue
        # берем строку только, если число в столбце телефонного номера       
        if (isinstance(row[0].value, int)
        or (isinstance(row[0].value, str) and row[0].value.isnumeric())):   
            string = ChargesTemp(
                period_date = date_from_file_name,
                number = row[0].value,
                charge = -row[charge_row].value,
            )
            session.add(string)
    session.commit()
    wb.close()
# СТАЛО
    # бывают разные названия листов, поэтому просто использую первый лист
    ws = wb[wb.sheetnames[0]]
    # столбец для суммы начислений рассчитывается в зависимости от заголовка;
    # всегда первая строка заголовок, вторая строка и далее данные 
    for i, row in enumerate(ws.rows):
        if i == 0 and row[2].value == "score_sum":      # столбец С
            charge_column = 2
            continue
        if i == 0 and row[2].value == "Сумма списаний": # столбец С
            charge_column = 2
            continue
        if i == 0 and row[3].value == "Общий итог":     # столбец E
            charge_column = 3
            continue
        if i == 0 and row[4].value == "Общий итог":     # столбец E
            charge_column = 4
            continue
        if i == 0 and row[6].value == "Общий итог":     # столбец G
            charge_column = 6
            continue
        if i == 0:
            raise "Ошибочный формат файла с начислениями по авансовым!"
            continue
        # в строках с начислениями в столбце номера телефона целое число
        is_row_with_accruals = isinstance(row[0].value, str) and row[0].value.isdigits()
        # собираем в таблицу только строки с начислениями (итоги не используем)
        if is_row_with_accruals:   
            string = ChargesTemp(period_date = date_from_file_name,
                                 # номер телефона всегда в столбце 0 (столбец A) 
                                 number = row[0].value,
                                 charge = -row[charge_column].value
                                )
            session.add(string)
    session.commit()
    wb.close()
# КОММЕНТАРИЙ:
# "8. Слишком много информации"
# - убрал тект про подготовку файлов
# "7. Избыточные комментарии"
# - убрал повторяющие код комментарии
# "1. Неочевидные комментарии"
# - перенес информацию про строку с подсчетом 
# общей суммы ближе к самому коду проверки
