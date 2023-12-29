"""
Types of data.
"""

# было
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# стало
import os
def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))
BASEDIR = get_basedir()
# дает полный путь к папке, где файл (без имени файла)
# инкапсулировал внутрь функции

# было
import os
# ...
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "for_report.db")
# стало
import os
# ...
SQLALCHEMY_DATABASE_NAME = "for_report.db"
def get_sqlalchemy_database_uri(basedir, database_name):
    return "sqlite:///" + os.path.join(basedir, database_name)
SQLALCHEMY_DATABASE_URI = get_sqlalchemy_database_uri(BASEDIR, SQLALCHEMY_DATABASE_NAME)
# путь, где находится база данных SQL
# инкапсулировал внутрь функции

# было (Access Basic из Microsoft Access 2.0)
If пПлан <> тПлан Or пКлиент <> тКлиент Or пБилл <> тБилл Or пСкидка <> тСкидка Or пVi <> тVi Or Day(пДатаИзм) = 1 Then
# стало
is_changed_tariff = previous_tariff != current_tariff
is_changed_client = previous_client != current_client
is_changed_calculate_status = previous_calculate_status != current_calculate_status
is_changed_discount = previous_discount != current_discount
is_changed_vi_status = previous_vi_status != previous_vi_status
is_previous_status_first_day_of_month = previous_status_date.day == 1
if (   is_changed_tariff 
    or is_changed_client
    or is_changed_calculate_status
    or is_changed_discount
    or is_changed_vi_status
    or is_previous_status_first_day_of_month
   ):
# выделяем период, если были изменения, либо он начинается в первый день месяца
# упрощение сложного условия

# было (Access Basic из Microsoft Access 2.0)
Dim ЕС_Минут As Double      'количество минут, которое уже накоплено на дату
Dim ЕС_МинутТП As Double    'количество минут в день, после которого начинается скидка
If ЕС_Минут >= ЕС_МинутТП Then
# стало
from decimal import Decimal
daily_discount_on_tariff_minutes = Decimal( # ...
daily_discount_accumulated_minutes = Decimal( # ...
if daily_discount_accumulated_minutes >= daily_discount_on_tariff_minutes:
# проверка, израсходован ли дневной лимит бесплатных минут
# изменил тип float на Decimal, для большей точности сравнений и для правильных округлений

# было (Access Basic из Microsoft Access 2.0)
X = IIf((X / Y) - Int(X / Y) = 0, X / Y, Int(X / Y) + 1) 'Размер фрагмента 
# стало
input_number_of_fragments = # ...
number_of_ctn_to_calculate = # ...
if input_number_of_fragments.isdigits():
    number_of_fragments = int(input_number_of_fragments)
else:
    number_of_fragments = 1
if number_of_fragments < 1 or number_of_fragments > 8:
    number_of_fragments = 1
if number_of_ctn_to_calculate % number_of_fragments == 0:
    number_of_ctn_in_fragment = number_of_ctn_to_calculate // number_of_fragments
else:
    number_of_ctn_in_fragment = number_of_ctn_to_calculate // number_of_fragments + 1
# расчет размера фрагмента (список номеров для многомашинного расчета разбивается на от 1 до 8 частей;
# количество фрагментов указывает пользователь; проверки корректности ввода не было)
# добавил проверку корректности ввода, чтобы не было возможности разделить на 0,
# также убрал сравнение вещественных чисел (при делении целочисленных получится вещественное)

# ниже придуманные примеры.

# было
BEGINNING_CONNECTION_FREE_SECONDS = 3
# ...
connection_duration_minutes = float( # ...
if (connection_duration_minutes * 60) < BEGINNING_CONNECTION_FREE_SECONDS:
    # ...
    # free connection
# стало
BEGINNING_CONNECTION_FREE_SECONDS = 3
# ...
connection_duration_minutes = float( # ...
connection_duration_seconds = int(connection_duration_minutes * 60)
if connection_duration_seconds < BEGINNING_CONNECTION_FREE_SECONDS:
    # ...
    # free connection
# бесплатное соединение продолжительностью менее 3 секунд
# сделал явное преобразование типов, также исключил сравнение значений разных типов

# было
screen_width_dots = int( # ...
number_of_columns = int( # ...
column_width_except_last_one = int(screen_width_dots / number_of_columns)
width_of_last_column = screen_width_dots - (number_of_columns - 1) * column_width_except_last_one
# стало
screen_width_dots = int( # ...
number_of_columns = int( # ...
column_width_except_last_one = screen_width_dots // number_of_columns
width_of_last_column = screen_width_dots - (number_of_columns - 1) * column_width_except_last_one
# нахождение ширин колонок (разбиваем экран на заданное число колонок)
# вместо получения вещественного частного и приведения его к целому применил целочисленное деление

# было
DISTANCE_TO_PLANET_KM = # ...
DISTANCE_FLOWN_IN_SECOND_KM = # ...
def calculates_how_much_distance_left_to_fly(flight_seconds):
    calculate_distance = DISTANCE_TO_PLANET_KM
    for _ in range(flight_seconds):
        calculate_distance -= DISTANCE_FLOWN_IN_SECOND_KM
    return calculate_distance
# стало
DISTANCE_TO_PLANET_KM = # ...
DISTANCE_FLOWN_IN_SECOND_KM = # ...
def calculates_how_much_distance_left_to_fly(flight_seconds):
    return DISTANCE_TO_PLANET_KM - flight_seconds * DISTANCE_FLOWN_IN_SECOND_KM
# функция вычисляет остаток пути до планеты для заданной секунды полёта
# убрал, насколько возможно, вычитание очень разных по величине чисел

# было
invoice_lines = [
                 {"product_name": "apple", "product_quantity": 7, "product_price_rub": 115.15},
                 {"product_name": "pear", "product_quantity": 3, "product_price_rub": 198.67},
                ]
def calculate_invoice_amount (invoice_lines):
    invoice_amount = 0.0
    for line_of_invoice in invoice_lines:
        invoice_amount += line_of_invoice["product_quantity"] * line_of_invoice["product_price_rub"]
    return invoice_amount
# стало
from decimal import Decimal
invoice_lines = [
                 {"product_name": "apple", "product_quantity": 7, "product_price_rub": Decimal("115.15")},
                 {"product_name": "pear", "product_quantity": 3, "product_price_rub": Decimal("198.67")},
                ]
def calculate_invoice_amount (invoice_lines):
    invoice_amount = Decimal("0.00")
    for line_of_invoice in invoice_lines:
        invoice_amount += round(line_of_invoice["product_quantity"] * line_of_invoice["product_price_rub"], 2)
    return round(invoice_amount, 2)
# функция подсчитывает общую сумму счета
# чтобы была корректная сумма сделал округление по строкам, округление общей суммы и перешел на тип Decimal

# было
if invoice_sum > Decimal("0.00") and (invoice_date.day() == 1 or invoice_date.day() > 25) and is_subscriber_VAT_payer:
# стало
is_non-zero_invoice = invoice_sum > Decimal("0.00")
is_invoice_was_issued_on_1st_or_later_than_25th = invoice_date.day() == 1 or invoice_date.day() > 25
if (    is_non-zero_invoice 
    and is_invoice_was_issued_on_1st_or_later_than_25th 
    and is_subscriber_VAT_payer
   ):
# использовал логические переменные для повышения читабельности программы

# было
if tariff_discount > subscriber_accumulated_discount and invoice_date.month() == 12 and calculate_days_in_year(invoice_date.year()) > 365:
# стало
is_discount_has_been_exceeded = tariff_discount > subscriber_accumulated_discount
is_month_December = invoice_date.month() == 12
is_leap_year = calculate_days_in_year(invoice_date.year()) > 365
if (is_discount_has_been_exceeded
    and is_month_December
    and is_leap_year):
# использовал логические переменные для повышения читабельности программы

# было
if is_goal_achievable and goal_date.month() = plan_date.month() and goal_date.year() = plan_date.year():
# стало
is_plan_and_goal_within_one_month = goal_date.month() = plan_date.month() and goal_date.year() = plan_date.year()
if is_goal_achievable and is_plan_and_goal_within_one_month:
# использовал логические переменные для повышения читабельности программы
