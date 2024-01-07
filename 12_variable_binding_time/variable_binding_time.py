"""
Variable binding time.
"""

# пример 1
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)
# функция добавляет к полученной дате заданное число месяцев;
# использую "магическое число" 12 - число месяцев в году;
# оно прописано в код, так как функция небольшая и вероятность
# изменения данного числа считаю крайне малой;
# возможно, стоит всё-таки сделать локальную константу (на уровне функции)
# не с целью вероятного изменения, а с целью именования,
# чтобы читающим код было быстрее его понять

# пример 2
PLANETS = {"Mercury": ephem.Mercury,
           "Venus":   ephem.Venus,
           "Earth":   ephem.Earth,
           "Mars":    ephem.Mars,
           "Jupiter": ephem.Jupiter,
           "Saturn":  ephem.Saturn,
           "Uranus":  ephem.Uranus,
           "Neptune": ephem.Neptune}
# ... много кода
    if PLANETS.get(text_list[1]) == None:
        update.message.reply_text(  "Ошибка в названии планеты. Попробуй еще раз. Нужно набрать /planet и название"
                                  + " планеты по-английски с большой буквы (например, '/planet Mars')."
                                 )
        return
    planet = PLANETS[text_list[1]](date.today())
# для телеграм-бота список планет - получение знака зодиака, в котором находится планета в заданную дату;
# использую константу, так как использую значение в двух местах, плюс есть небольшая вероятность изменения:
# 1) Плутон не так давно лишился статуса планеты
# 2) названия методов могут измениться при изменении библиотеки

# пример 3 - вариант 1
import os
def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))
BASEDIR = get_basedir()
# папки с исходными данными и результатом находятся внутри папки с программой
# поэтому на этапе инициализации сохраняю в переменную (в константу?) 
# путь к папке, откуда запущена программа

# пример 3 - вариант 2
# ... много кода
            # вычисляем номера столбцов для номера телефона и для начислений
            if row[0].value == "Номер абонента":
                number_row = 0
            elif row[0].value == "Номер":
                number_row = 0
            elif row[1].value == "Номер абонента":
                number_row = 1
            elif row[1].value == "Номер":
                number_row = 1
            elif row[1].value == "Номер абонента\nmsisdn\n[#1917]":
                number_row = 1
            elif row[2].value == "Номер абонента\nmsisdn\n[#1917]":
                number_row = 2
            elif row[2].value == "Номер абонента":
                number_row = 2
            else:
                raise "Ошибочный формат файла с начислениями по кредитным!"
# ... много кода
# к сожалению формат исходного файла "поставщики" периодически меняют,
# определять номер нужного столбца приходится эмпирически по заголовку 
# уже в процессе работы программы, а, если ни один формат не подходит, 
# выдавать ошибку времени исполнения
