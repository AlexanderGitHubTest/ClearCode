"""
Arrays.
"""

# пример 1
# БЫЛО
"""
Функция проверяет, что список из 5 строк является
строкой из раздела 'Разовые начисления'.
Проверки следующие:
- все 5 строк не None
- первое значение попадает под маску 'ровно 10 цифр'
- второе значение не None
- третье и четвертое значения типа Float (можно конвертировать)
- пятое значение можно конвертировать в integer
Если все проверки прошли, то возвращается True, иначе False
"""
def check_for_line_in_block_onetime_charges(list_of_5_strings):
    for string in list_of_5_strings:
        if string == None:
            return False
    if not (list_of_5_strings[0].isdigit() and len(list_of_5_strings[0]) == 10):
        return False
    if re.match(r"^-?\d+(?:\.\d+)$", list_of_5_strings[2]) is None:
        return False
    if re.match(r"^-?\d+(?:\.\d+)$", list_of_5_strings[3]) is None:
        return False
    # в количестве бывает цифра в виде "   1", поэтому функция strip
    if not list_of_5_strings[4].strip().isdigit():
        return False
    return True
# Функция ищет строки со словами "ПриорОбслАгент"
# Возвращает по каждому нахождению словарь из 5 позиций:
# phone - номер телефона
# from_date - с какой даты
# to_date - по какую дату
# service_name - название услуги
# fee - начисления по услуге
# При нахождении строки "Детализация" прекращает работу
# (чтобы обрабатывать только приложение к счету)
# Реализация. Запоминаем 5 предыдущих строк. И последовательно сдвигаем
# Если в 5-й строке "ПриорОбсАгент", то формируем выходную строку
def agprior_searching(list_of_strings):
    list_of_6_strings = [None, None, None, None, None, None]
    # Буду ставить в True после строки "Разовые начисления"
    # Буду возвращать в False после строки "Приложение к счету №"
    # Буду возвращать в False после строки "Скидки и надбавки"
    # Буду возвращать в False после строки "Перенос начислений в Единый счет"
    onetime_charges = False
    for string in list_of_strings:
        if string.find("Разовые начисления") != -1:
            onetime_charges = True
        if string.find("Приложение к счету №") != -1:
            onetime_charges = False
        if string.find("Cкидки и надбавки") != -1:
            onetime_charges = False
        if string.find("Перенос начислений в Единый счет") != -1:
            onetime_charges = False
        if string.find("Использование включённого трафика и корректировки") != -1:
            print("Использование включённого трафика и корректировки")
            break
        if string.find("Детализация") != -1:
            print("Детализация")
            break
        elif list_of_6_strings[0] is None:
            list_of_6_strings[0] = string
        elif list_of_6_strings[1] is None:
            list_of_6_strings[1] = string
        elif list_of_6_strings[2] is None:
            list_of_6_strings[2] = string
        elif list_of_6_strings[3] is None:
            list_of_6_strings[3] = string
        elif list_of_6_strings[4] is None:
            list_of_6_strings[4] = string
        else:
            if list_of_6_strings[5] is not None:
                # если в последней ячейке что-то есть, делаю сдвиг
                list_of_6_strings[0] = list_of_6_strings[1]
                list_of_6_strings[1] = list_of_6_strings[2]
                list_of_6_strings[2] = list_of_6_strings[3]
                list_of_6_strings[3] = list_of_6_strings[4]
                list_of_6_strings[4] = list_of_6_strings[5]
            list_of_6_strings[5] = string
            if list_of_6_strings[4].find("ПриорОбслАгент") != -1:
                # print(list_of_6_strings[4])
                yield {
                    "phone": list_of_6_strings[0],
                    "from_date": list_of_6_strings[1],
                    "to_date": list_of_6_strings[3],
                    "service_name": list_of_6_strings[4],
                    # меняем точку на запятую, чтобы excel корректно читал
                    "fee": list_of_6_strings[5].replace(".", ","),
                    "type": "agprior"
                    }
            elif onetime_charges:
                if check_for_line_in_block_onetime_charges(list_of_6_strings[:5]):
                    yield {
                        "phone": list_of_6_strings[0],
                        "description": list_of_6_strings[1],
                        # меняем точку на запятую, чтобы excel корректно читал
                        "charge": list_of_6_strings[2].replace(".", ","),
                        "quantity": list_of_6_strings[4].strip(),
                        # меняем точку на запятую, чтобы excel корректно читал
                        "summa": list_of_6_strings[3].replace(".", ","),
                        "type": "one_time_charges"
                    }
# СТАЛО
def agprior_searching(list_of_strings):
    """
    Функция ищет строки по заданым шаблонам.
    Сейчас реализован поиск двух шаблонов.
    1) Строки со словами "ПриорОбслАгент":
    Возвращает по каждому нахождению словарь из 5 позиций:
    phone - номер телефона
    from_date - с какой даты
    to_date - по какую дату
    service_name - название услуги
    fee - начисления по услуге
    При нахождении строки "Детализация" прекращает работу
    (чтобы обрабатывать только приложение к счету)
    2) Что строка является строкой из раздела 'Разовые начисления'.
    Проверки следующие:
    - все 5 строк не None
    - первое значение попадает под маску 'ровно 10 цифр'
    - второе значение не None
    - третье и четвертое значения типа Float (можно конвертировать)
    - пятое значение можно конвертировать в integer
    Возвращает по каждому нахождению словарь из 5 позиций.
    """
    # -= check string functions block begin =-
    def check_string_has_agprior_text(string):
        if string == None:
            return False
        if string.find("ПриорОбслАгент") != -1:
            return True
        return False
    def check_string_has_float_value(string):
        if string == None:
            return False
        if re.match(r"^-?\d+(?:\.\d+)$", string) is None:
            return False
        return True
    def check_string_has_only_ten_digits(string):
        if string == None:
            return False
        if (    string.isdigit() 
            and len(string) == 10
           ):
            return True
        return False
    def check_string_has_integer_value(string):
        if string == None:
            return False
        # в количестве бывает цифра в виде "   1", поэтому функция strip
        if string.strip().isdigit():
            return True
        return False
    # -= check string functions block end =-
    # -= clear functions block begin =-
    def clear_agprior_variables():
        nonlocal agprior_templates
        nonlocal agprior_row
        agprior_row.clear()
        agprior_templates["is_first_column_not_none"] = False
        agprior_templates["is_second_column_not_none"] = False
        agprior_templates["is_third_column_not_none"] = False
        agprior_templates["is_fourth_column_not_none"] = False
        agprior_templates["is_fifth_column_has_agprior_text"] = False
    def clear_otc_variables():
        nonlocal otc_templates
        nonlocal otc_row
        otc_row.clear()
        otc_templates["is_first_column_has_ten_digits"] = False
        otc_templates["is_second_column_not_none"] = False
        otc_templates["is_third_column_has_float_value"] = False
        otc_templates["is_fourth_column_has_float_value"] = False        
    # -= clear functions block end =-
    # -= check row functions block begin =-
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
    # -= check row functions block end =-
    # -= main block begin =-
    from collections import deque
    agprior_templates = {"is_first_column_not_none": False,
                         "is_second_column_not_none": False,
                         "is_third_column_not_none": False,
                         "is_fourth_column_not_none": False,
                         "is_fifth_column_has_agprior_text": False}
    otc_templates = {"is_first_column_has_ten_digits": False,
                     "is_second_column_not_none": False,
                     "is_third_column_has_float_value": False,
                     "is_fourth_column_has_float_value": False}
    agprior_row = deqie()
    otc_row = deqie()
    is_otc_section_now = False
    for string in list_of_strings:
        if string.find("Разовые начисления") != -1:
            is_otc_section_now = True
        if (   string.find("Приложение к счету №") != -1
            or string.find("Cкидки и надбавки") != -1
            or string.find("Перенос начислений в Единый счет") != -1
           ):
            is_otc_section_now = False
        if (   string.find("Использование включённого трафика и корректировки") != -1
            or string.find("Детализация") != -1
           ):
            break
        check_if_row_is_agprior_row(string)
        if is_otc_section_now:
            check_if_row_is_otc_row(string)
    # -= main block end =-

# пример 2
# БЫЛО
def square_free_part(n):
    """
    Squarefree Part of a Number
    """
    divisors = []
    if n == 1:
        return 1
    else:
        for i in range(2,n):
            if n % i == 0: divisors.append(i)
        divisors.append(n)
        for i, divisor in enumerate(divisors):
            sqrt_ = int(divisor ** 0.5)
            if sqrt_ * sqrt_ == divisor:
                for j, divisor2 in enumerate(divisors):
                    if j>=i and divisor2 % divisor == 0: divisors[j] = divisor2 // divisor
        return max(divisors)
# СТАЛО
def square_free_part(n):
    """
    Squarefree Part of a Number
    """
    if n == 1:
        return 1
    from collections import deque
    original_divisors = deque()
    for i in range(2, n//2 + 1):
        if n % i == 0: 
            original_divisors.append(i)
    original_divisors.append(n)
    final_divisors = deque()
    squares_of_divisors = deque()
    while original_divisors:
        divisor = original_divisors.popleft()
        divisor_without_squares = divisor
        for square in squares_of_divisors:
            if divisor_without_squares % square == 0:
                divisor_without_squares = divisor_without_squares // square
        sqrt_ = int(divisor ** 0.5)
        if sqrt_ * sqrt_ == divisor:
            final_divisors.append(1) # divisor // divisor = 1
            squares_of_divisors.append(divisor_without_squares)
            continue
        final_divisors.append(divisor_without_squares)
    return max(final_divisors)

# пример 3
# БЫЛО
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def keyword_cipher(msg, keyword):
    """
    Keyword Cipher
    """
    encrypted_string = list(x[1] for x in filter(lambda x: (x[0] < 2), ((keyword[:i+1].count(s), s) for i, s in enumerate(keyword))))
    encrypted_string.extend(filter(lambda x: x not in encrypted_string, ALPHABET))
    return ''.join(list(encrypted_string[ALPHABET.find(x)] if x in ALPHABET else x for x in msg.lower()))
# СТАЛО
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def keyword_cipher(msg, keyword):
    """
    Keyword Cipher
    """
    from collections import deque
    encryption_key = deque()
    used_letters_in_keyword = set()
    for letter in keyword + ALPHABET:
        if letter not in used_letters_in_keyword:
            encryption_key.append(letter)
            used_letters_in_keyword.add(letter)
    encryption_dict = {}
    for letter in ALPHABET:
        encryption_dict[letter] = encryption_key.popleft()
    result_string = ""
    for letter in msg.lower():
        if letter == " ":
            result_string += " "
            continue
        result_string += encryption_dict[letter]
    return result_string

# пример 4
# БЫЛО
def solution(args):
    """
    Range Extraction
    """
    l = []
    result = []
    for number in args:
        if l == []: 
            l.append(number)
        elif l[-1] + 1 == number:
            l.append(number)
        else:
            if len(l) < 3:
                result.extend(str(x) for x in l)
            else:
                result.append(str(l[0]) + "-" + str(l[-1]))
            l=[]
            l.append(number)
    if len(l) < 3:
        result.extend(str(x) for x in l)
    else:
        result.append(str(l[0]) + "-" + str(l[-1]))
    return ",".join(result)
# СТАЛО
def solution(args):
    """
    Range Extraction
    """
    from collections import deque
    l = deque()
    result = deque()
    for number in args:
        if not l: 
            l.append(number)
            continue
        last_element = l.pop()
        l.append(last_element)
        if last_element + 1 == number:
            l.append(number)
            continue
        if len(l) < 3:
            result.extend(str(x) for x in l)
        if len(l) >= 3:
            result.append(str(l.popleft()) + "-" + str(l.pop()))
        l.clear()
        l.append(number)
    if len(l) < 3:
        result.extend(str(x) for x in l)
    if len(l) >= 3:
        result.append(str(l.popleft()) + "-" + str(l.pop()))
    return ",".join(result)

# пример 5 (придуманный)
# БЫЛО
def get_snake_of_letters(square_of_letters):
    """
    Функция получает квадрат из букв (список списков).
    Функция возвращает 'змейку' из букв.
    Змейка собирается по спирали с центра квадрата для нечетных квадратов
    (для квадратов с четной длиной стороны начальный квадрат слева-сверху от центра).
    Направление обхода вправо-вниз-влево-вверх.
    Пример. 
    Для квадрата [[1, 2, 3], [4, 5, 6], [7, 8, 9]] функция вернёт '569874123'.
    """
    dimension = len(square_of_letters)
    if dimension == 0:
        return ""
    if dimension == 1:
        return square_of_letters[0][0]
    resulting_string = ""
    # координаты центра
    coordinate_x = (dimension - 2 + (dimension % 2)) // 2
    coordinate_y = (dimension - 2 + (dimension % 2)) // 2
    resulting_string = str(square_of_letters[coordinate_y][coordinate_x])
    for i in range(2, dimension + 1):
        if i % 2 == 0:
            coordinate_x += 1
            resulting_string += str(square_of_letters[coordinate_y][coordinate_x])
            for _ in range(i - 1):
                coordinate_y += 1
                resulting_string += str(square_of_letters[coordinate_y][coordinate_x])
            for _ in range(i - 1):
                coordinate_x -= 1
                resulting_string += str(square_of_letters[coordinate_y][coordinate_x])
            continue
        coordinate_x -= 1
        resulting_string += str(square_of_letters[coordinate_y][coordinate_x])
        for _ in range(i - 1):
            coordinate_y -= 1
            resulting_string += str(square_of_letters[coordinate_y][coordinate_x])
        for _ in range(i - 1):
            coordinate_x += 1
            resulting_string += str(square_of_letters[coordinate_y][coordinate_x])
    return resulting_string
# СТАЛО
def get_snake_of_letters(square_of_letters):
    """
    Функция получает квадрат из букв (список списков).
    Функция возвращает 'змейку' из букв.
    Змейка собирается по спирали с центра квадрата для нечетных квадратов
    (для квадратов с четной длиной стороны начальный квадрат слева-сверху от центра).
    Направление обхода вправо-вниз-влево-вверх.
    Пример. 
    Для квадрата [[1, 2, 3], [4, 5, 6], [7, 8, 9]] функция вернёт '569874123'.
    """
    dimension = len(square_of_letters)
    if dimension == 0:
        return ""
    if dimension == 1:
        return square_of_letters[0][0]
    from collections import deque
    resulting = deque()
    # координаты центра
    coordinate_x = (dimension - 2 + (dimension % 2)) // 2
    coordinate_y = (dimension - 2 + (dimension % 2)) // 2
    resulting.append(square_of_letters[coordinate_y][coordinate_x])
    for i in range(2, dimension + 1):
        if i % 2 == 0:
            coordinate_x += 1
            resulting.append(square_of_letters[coordinate_y][coordinate_x])
            for _ in range(i - 1):
                coordinate_y += 1
                resulting.append(square_of_letters[coordinate_y][coordinate_x])
            for _ in range(i - 1):
                coordinate_x -= 1
                resulting.append(square_of_letters[coordinate_y][coordinate_x])
            continue
        coordinate_x -= 1
        resulting.append(square_of_letters[coordinate_y][coordinate_x])
        for _ in range(i - 1):
            coordinate_y -= 1
            resulting.append(square_of_letters[coordinate_y][coordinate_x])
        for _ in range(i - 1):
            coordinate_x += 1
            resulting.append(square_of_letters[coordinate_y][coordinate_x])
    resulting_string = ""
    for _ in range(len(resulting)):
        resulting_string += str(resulting.popleft())
    return resulting_string
