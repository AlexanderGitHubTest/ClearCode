"""
Comments.
"""

# 3.1. Прокомментируйте 7 мест в своём коде там, где это явно уместно.
# комментарий 1
# БЫЛО
            for col in range(len_period_names - 
                (lambda last_period: 0 if last_period else 1)(
                section["output_the_last_period"])):
# СТАЛО
            # для секций, где НЕ нужен вывод последнего периода,
            # не учитывать его при переборе периодов
            for col in range(len_period_names - 
                (lambda last_period: 0 if last_period else 1)(
                section["output_the_last_period"])):
# КОММЕНТАРИЙ К КОММЕНТАРИЮ:
# 1) output_the_last_period - правильнее назвать is_needed_output_of_last_period
# 2) конструкцию вообще бы переделать без lambda 
# (например, в константу output_the_last_period не булевское значение писать, а сразу число)


# комментарий 2
# БЫЛО
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
# СТАЛО
                # Здесь выбор из 4 вариантов, основываясь на комбинациях 
                # worksheet_need и return_name
                # worksheet_need - булевская
                #                  False, когда ячейка "первичная", то есть расчет идёт просто на основе периода
                #                  (ячейка не зависит от других ячеек)
                #                  True, когда ячейка расчетная, тогда в расчитывающую функцию передаем
                #                  лист Excel
                # return_name - принимает значения None или ключ в тексовом формате
                #               None - когда функция возвращает само значение
                #               Ключ - когда функция возвращает словарь и нужное значение из словаря
                #               получаем по ключу
                worksheet_need = section["worksheet_need"]        
                return_name = section["functon_returns_name"]                
                # ... далее продолжается код, который в "БЫЛО"
# КОММЕНТАРИЙ К КОММЕНТАРИЮ:
# Этот блок переделать бы:
# 1) Сложные "многовложенные" if
# 2) Отдельные переменные worksheet_need и return_name лишние, они не дают сильно упрощения
# 3) section["functon_returns_name"] нужно разделить на несколько, так как переменная (константа) несёт
# сразу несколько разных смыслов
# 4) может как-то по-другому реализовать вообще весь блок; идея была в том, чтобы просто перебирать
# функции и заполнять лист excel, но из-за разных сильно разных функций появилась вот такая сложность

# комментарий 3
# БЫЛО
csv.register_dialect("my_dialect", delimiter=";", lineterminator="\n")
# СТАЛО
# объявляем свой dialect, так как ни один сущестующий не подходит
csv.register_dialect("my_dialect", delimiter=";", lineterminator="\n")

# комментарий 4
# БЫЛО
    def check_if_row_is_agprior_row(string):
        nonlocal agprior_templates
        nonlocal agprior_row
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
# СТАЛО
    def check_if_row_is_agprior_row(string):
        """
        Проверяем, что строка является строкой с agprior начислениями:
        - первые 4 столбца не пустые;
        - 5-й столбец содержит текст 'ПриорОбслАгент';
        - 6-й столбкц содержит float значение
        """
        # ... дальше код функции
# КОММЕНТАРИЙ К КОММЕНТАРИЮ:
# 1) надо бы для check_string_has_agprior_text(string) сделать
# искомый текст параметром;
# 2) вообще хочется как-то упростить функцию, чтобы было не нагромождение if,
# а прозрачнее, но как это сделать, пока не знаю
# 3) не нравится, что все проверки, кроме последней, отражены в словаре agprior_templates,
# а последняя проверка не отражена, какой-то стройности не хватает.

# комментарий 5
# БЫЛО
    def check_if_row_is_otc_row(string)
        nonlocal agprior_templates
        nonlocal agprior row
        if (    otc_templates["is_fourth_column_has_float_value"]
            and check_string_has_integer_value(string)
           ):
            yield {"quantity": string.strip(), 
                   # меняем точку на запятую, чтобы excel корректно читал                  
                   "summa": otc_row.pop().replace(".", ","),                   
                   # меняем точку на запятую, чтобы excel корректно читал
                   "charge": otc_row.pop().replace(".", ","),                   
                   "description": otc_row.pop(),
                   "phone": otc_row.pop()
                   "type": "one_time_charges"
                  }
            clear_otc_variables()
            return
        if (    agprior_templates["is_third_column_has_float_value"]
            and check_string_has_float_value(string)
           ):
            otc_templates["is_fourth_column_has_float_value"] = True
            otc_row.append(string)
            return
        if (    otc_templates["is_second_column_not_none"]
            and check_string_has_float_value(string)
           ):
            otc_templates["is_third_column_has_float_value"] = True
            otc_row.append(string)
            return
        if (    otc_templates["is_first_column_has_ten_digits"]
            and string != None
           ):
            otc_templates["is_second_column_not_none"] = True
            otc_row.append(string)
            return
        if check_string_has_only_ten_digits(string):
            otc_templates["is_first_column_has_ten_digits"] = True
            otc_row.append(string)
            return
        clear_otc_variables()
# СТАЛО
    def check_if_row_is_otc_row(string)
        """
        Проверяем, что строка является строкой с otc ('one time charges') начислениями:
        - 1-й столбец содержит ровно 10 цифр;
        - 2-й столбец не пустой;
        - 3-й и 4-й столбцы содержат float значение;
        - 5-й столбкц содержит integer значение (при этом могут быть пробелы впереди).
        """
        # ... дальше код функции
# КОММЕНТАРИЙ К КОММЕНТАРИЮ:
# 1) вообще хочется как-то упростить функцию, чтобы было не нагромождение if,
# а прозрачнее, но как это сделать, пока не знаю
# 2) не нравится, что все проверки, кроме последней, отражены в словаре otc_templates,
# а последняя проверка не отражена, какой-то стройности не хватает.
# 3) относится и к 4-му комментарию. Проверки на agprior и otc собраны в одной функции,
# может быть как-то их разделить?

# комментарий 6
# БЫЛО
def find_text_strings(stream_line_decode):
    # позиция начала текста в потоке
    pos_begin = stream_line_decode.find(b"TD\n(")
    while pos_begin != -1:
        # скобка ')' - конец текста
        pos_end = stream_line_decode.find(b")", pos_begin)
        # но встречаются последовательности '\\)' -
        # такое является частью текста,
        # соответственно, проверяю найденное вхождение,
        # если оно часть текста, то двигаю pos_end
        while (stream_line_decode
               .find(b"\\)", pos_end - 1, pos_end + 1) 
               != -1
              ):
            pos_end = stream_line_decode.find(b")", pos_end + 1)
        yield (stream_line_decode[pos_begin+4: pos_end]
               .replace(b"\\)",b")")
               .replace(b"\\(", b"(")
               .decode("1251")
              )
        pos_begin = stream_line_decode.find(b"TD\n(",
                                            pos_begin + 1
                                           )
# СТАЛО
def find_text_strings(stream_line_decode):
    # позиция начала текста в потоке
    pos_begin = stream_line_decode.find(b"TD\n(")
    while pos_begin != -1:
        # скобка ')' - конец текста
        pos_end = stream_line_decode.find(b")", pos_begin)
        # но встречаются последовательности '\\)' -
        # такое является частью текста, а не концом текста,
        # поэтому поиск нужно продолжать,
        # пока не переберём все '\\)'
        while (stream_line_decode
               .find(b"\\)", pos_end - 1, pos_end + 1) 
               != -1
              ):
            pos_end = stream_line_decode.find(b")", pos_end + 1)
        # комбинации "\\)" и "\\(" - это такая кодировка скобок,
        # поэтому преобразуем их просто в скобки
        yield (stream_line_decode[pos_begin+4: pos_end]
               .replace(b"\\)",b")")
               .replace(b"\\(", b"(")
               .decode("1251")
              )
        pos_begin = stream_line_decode.find(b"TD\n(",
                                            pos_begin + 1
                                           )
# КОММЕНТАРИЙ К КОММЕНТАРИЮ:
# комментарии были непонятные, поэтому изменил их и добавил еще дополнительные;
# весь блок переписать бы, так как очень он "путанный" и без комментариев
# плохо воспринимается

# комментарий 7
# БЫЛО
# Вычисляет поле correction
def calculate_correction(fee, summa):
    if summa == None:
        return None
    elif summa >= 0.0:
        return 0.0
    elif -summa >= fee:
        return fee
    else:
        return -summa
# СТАЛО
def calculate_correction(fee, summa):
    """
    Вычисляет поле correction.
    fee - начисления по AGPRIOR (они всегда положительны)
    summa - коррекция начислений (коррекция, только если summa < 0)
    Если summa отрицательная, то функция выдает меньшее (по модулю) из 
    двух значений: summa или fee
    """
    if summa == None:
        return None
    if summa >= 0.0:
        return 0.0
    if -summa >= fee:
        return fee
    return -summa
# КОММЕНТАРИЙ К КОММЕНТАРИЮ:
# наверное, через min нужно переписать последний if, чтобы было прозрачнее

# 3.2. Если вы раньше делали комментарии к коду, найдите 5 мест, где эти комментарии были излишни, удалите их и сделайте сам код более наглядным.

# Общий комментарий по 3.2. Нашёл только одно место и то спорное. Комментариев в коде пишу много, но они
# не про прояснение кода, а про алгоритм решения, либо про условия задачи, либо описание функций и переменных, 
# либо этакий справочник по python для себя внутри кода. Насколько понял смысл задания, нужно убирать комментарии,
# которые именно проясняют решение в коде.

# пример 1
# БЫЛО
            # уберем нули слева в строке (чтобы не загружать номера типа
            # "0000000000", "0881111706" и т.п.)
            # берем строку только, если число в столбце телефонного номера
            # и длина строки равна 10 символам
            number_lstrip_0 = line[0].lstrip("0")
            if number_lstrip_0.isnumeric() and len(number_lstrip_0) == 10:
# СТАЛО
            is_client_phone_number = line[0].isnumeric() and len(line[0].lstrip("0")) == 10
            # проверить, клиентский ли это номер
            if is_client_phone_number:
