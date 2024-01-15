"""
Correct Comments.
"""

# правка 1
def pdfrw_read(file):
    """
    Вместо собственного разбора стал использовать библиотеку 
    pdfrw для чтения потоков из pdf файла.
    Возвращает распакованное содержимое stream
    Выходной формат оставил такой же, как у функции line_marking,
    Но физически наличие stream у страницы и что
    есть флаг /Filter /FlatDecode не проверяется
    (если будет где-то страница без этого, то ошибка будет)
    """
    # TODO - текущие файлы все проходят, но нужно сделать
    # проверку на наличие у страницы stream и флагов /Filter и /FlatDecode,
    # вдруг попадется файл другого формата.
    from pdfrw import PdfReader
    fdata = file.read()
    x = PdfReader(fdata=fdata)
    for page in x.pages:
        stream_line = bytes(page.Contents.stream, 'latin-1')
        yield {
                    "object_type": "stream_line",
                    "stream_line": stream_line,
                    "flags": {"filter": True}
                    }
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "6. Комментарии TODO"
# добавил блок TODO после описания функции

# правка 2
        # если содержимое строки не соответствует типу float
        # (соответствие типу float: опционально знак минус "-", 
        # далее одна или более цифр, далее точка ".", 
        # после точки одна или более цифр)
        if re.match(r"^-?\d+(?:\.\d+)$", string) is None:
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "1. Информативные комментарии"
# добавил информативный комментарий касательно регулярного выражения

# правка 3
    def check_if_row_is_agprior_row(string):
    """
    Проверить, является ли строка строкой с начислениями типа AGPRIOR.
    """
        nonlocal agprior_templates
        nonlocal agprior_row
        # функция заполняет agprior_templates на основании поступающих 
        # текстовых значений (сначала is_first_column...,
        # затем is_second_column.. и т.д.);
        # другими словами, если "первый" прошёл проверку и "второй" прошёл
        # проверку и ... ... "шестой" прошёл проверку, то значит,
        # это нужная строка. Если какой-то элемент не прошёл проверку,
        # то делается полный сброс agprior_templates
        if (    agprior_templates["is_fifth_column_has_agprior_text"]
            and check_string_has_float_value(string)
           ):
            yield {# меняем точку на запятую, чтобы excel корректно читал
                   "fee": string.replace(".", ","),
                   "type": "agprior",
                   "service_name": agprior_row.pop(),
                   "to_date": agprior_row.pop(),
                   "phone": agprior_row.popleft(),
                   "from_date": agprior_row.popleft()
                  }
            clear_agprior_variables()
            return
        if (    agprior_templates["is_fourth_column_not_none"]
            and check_string_has_agprior_text(string)
           ):
            agprior_templates["is_fifth_column_has_agprior_text"] = True
            agprior_row.append(string)
            return
        if (    agprior_templates["is_third_column_not_none"]
            and string != None
           ):
            agprior_templates["is_fourth_column_not_none"] = True
            agprior_row.append(string)
            return
        if (    agprior_templates["is_second_column_not_none"]
            and string != None
           ):
            agprior_templates["is_third_column_not_none"] = True
            agprior_row.append(string)
            return
        if (    agprior_templates["is_first_column_not_none"]
            and string != None
           ):
            agprior_templates["is_second_column_not_none"] = True
            agprior_row.append(string)
            return
        if string != None:
            agprior_templates["is_first_column_not_none"] = True
            agprior_row.append(string)
            return
        clear_agprior_variables()
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "1. Информативные комментарии"
# добавил информативный комментарий касательно алгоритма проверки

# правка 4
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
# ... много кода
def button(update, bot):
    # update - объект "входящее обновление"
    # callback_query - объект "вызов с кнопки на интерактивной клавиатуре"
    query = update.callback_query
    # chat_id - уникальный идентификатор чата (тип int)
    chat_id = query.message.chat_id
    # data - данные, связанные с кнопкой на интерактивной клавиатуре,
    # содержит текст callback_data, который был передан объекту InlineKeyboardButton
    variant = query.data
    # `CallbackQueries` требует ответа, даже если 
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы. 
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "3. Прояснение"
# добавил комментарии для прояснения использования библиотеки telegram

# правка 5
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
# ... много кода
    # Updater - объект, получающий обновления от Telegram
    mybot = Updater(<"уникальный код">)
    # dispatcher - диспетчер, который обрабатывает обновления и отправляет их обработчикам.
    dp = mybot.dispatcher
    # add_handler - регистрирует обработчик
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("planet", in_which_constellation_is_the_planet))
    dp.add_handler(CommandHandler("dog", random_dog))
    # start_polling запускает опрос обновлений из Telegram
    mybot.start_polling()
    # обработка нажатия Ctrl-C
    mybot.idle()
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "3. Прояснение"
# добавил комментарии для прояснения использования библиотеки telegram

# правка 6
class AgpriorGrp(Base):
    """
    Класс содержит временную таблицу - результат группировки таблицы Agprior
    """
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "1. Информативные комментарии"
# добавил информативный комментарий для прояснения смысла таблицы AgpriorGrp

# правка 7
# Создадим таблицы с группированными данными для agprior и onecharge
# TODO - реализовано крайне неоптимальным образом (построчным перебором)
# для текущих задач скорость нормальная, но, по-хорошему, 
# переделать бы на формирование группировки запросом, 
# так как на больших таблицах будет очень медленно
sql_groupping_agprior = session.query(Agprior.phone, func.sum(Agprior.fee)).group_by(Agprior.phone)
for row in sql_groupping_agprior:
    string = AgpriorGrp(
        phone=row[0],
        fee=row[1]
    )
    session.add(string)
session.commit()
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "6. Комментарии TODO"
# добавил блок TODO про производительность блока кода

# правка 8
# Блок считывает входящие pdf файлы, обрабатывает каждый последовательными генераторами
# с целью нахождения строк по шаблонам "agprior" и "one time charges";
# найденные строки для каждого из шаблона записываются в свой csv файл
list_of_pdf = glob("pdf\\*.pdf")
for pdf_file in list_of_pdf:
    with open(pdf_file, "rb") as f:
        line_with_obj = pdfrw_read(f)
        decoding_line = stream_decoding(line_with_obj)
        agprior_line = agprior_searching(decoding_line)
        with open(FILE_NAME_AGPRIOR, "a", encoding="1251") as f_out:
            writer = csv.DictWriter(f_out, fields, dialect="my_dialect")
            with open(FILE_NAME_ONE_TIME_CHARGE, "a", encoding="1251") as f_otc_out:
                writer_otc = csv.DictWriter(f_otc_out, fields_otc, dialect="my_dialect")
                for line in agprior_line:
                    if line["type"] == "agprior":
                        writer.writerow(line)
                    else:
                        if line["description"] == "Абонентская плата за дополнительные услуги":
                            writer_otc.writerow(line)
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "3. Прояснение"
# добавил комментарии, проясняющие работу сложного блока

# правка 9
# TODO - слишком большая вложенность (for - with - with - with - for - if - else - if)
# Блок разбить бы на меньшие части
list_of_pdf = glob("pdf\\*.pdf")
for pdf_file in list_of_pdf:
    with open(pdf_file, "rb") as f:
        line_with_obj = pdfrw_read(f)
        decoding_line = stream_decoding(line_with_obj)
        agprior_line = agprior_searching(decoding_line)
        with open(FILE_NAME_AGPRIOR, "a", encoding="1251") as f_out:
            writer = csv.DictWriter(f_out, fields, dialect="my_dialect")
            with open(FILE_NAME_ONE_TIME_CHARGE, "a", encoding="1251") as f_otc_out:
                writer_otc = csv.DictWriter(f_otc_out, fields_otc, dialect="my_dialect")
                for line in agprior_line:
                    if line["type"] == "agprior":
                        writer.writerow(line)
                    else:
                        if line["description"] == "Абонентская плата за дополнительные услуги":
                            writer_otc.writerow(line)
# КОММЕНТАРИЙ К КОММЕНТАРИЯМ:
# согласно пункта "6. Комментарии TODO"
# добавил блок TODO про слишком большую сложность (вложенность) блока кода

# правка 10
    # TODO - слишком большая вложенность (for - if - for - if - else - if)
    # Блок разбить бы на меньшие части
    for section in REPORT_SECTIONS:
        if section["output_to_report"]:
            _ = ws.cell(column=1, 
                row=section["row_for_excel"], 
                value=section["section_name_for_report"])
            for col in range(len_period_names - 
                (lambda last_period: 0 if last_period else 1)(
                section["output_the_last_period"])):
                worksheet_need = section["worksheet_need"]
                return_name = section["functon_returns_name"]
                if return_name == None:
                    if worksheet_need:
                        _ = ws.cell(column=col+2,
                        row=section["row_for_excel"], 
                        value=section["function_name"](col, ws, REPORT_SECTIONS))
                    else:
                        _ = ws.cell(column=col+2,
                        row=section["row_for_excel"], 
                        value=section["function_name"](period_names[col].period_name))
                else:
                    if worksheet_need:
                        _ = ws.cell(column=col+2,
                        row=section["row_for_excel"], 
                        value=section["function_name"](col, ws, REPORT_SECTIONS)[return_name])
                    else:
                        function_return = section["function_name"](period_names[col].period_name)
                        _ = ws.cell(column=col+2,
                        row=section["row_for_excel"],  
                        value=function_return[return_name])
                        if EXTENDED_RESULT and section["query_returns_name"] != None:
                            _ = query_to_xlsx(function_return[section["query_returns_name"]], 
                                            QUERY_OUTPUT_FILES_PATH, 
                                            str(period_names[col].period_name)[:7], 
                                            section["section_id"])
                # ... еще код
# согласно пункта "6. Комментарии TODO"
# добавил блок TODO про слишком большую сложность (вложенность) блока кода

# правка 11
    for col in range(len_period_names):
        # форматирование строки периодов
        # пример формата периода: "Апрель 2021"
        ws[
            f"{utils.cell.get_column_letter(col+2)}{1}"
        ].number_format = "mmmm yyyy;@"
# согласно пункта "1. Информативные комментарии"
# добавил информативный комментарий - пример получающегося формата

# правка 12
    # - color="000000" - это чёрный цвет рамки
    thins = Side(border_style="thin", color="000000")
# согласно пункта "1. Информативные комментарии"
# добавил информативный комментарий - название цвета для "магической" константы
