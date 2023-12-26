"""
Constants.
"""


fields - AGPRIOR_CSV_HEADER_FIELDS
# список полей (list) для "шапки" результирующего csv файла по категории AGPRIOR

fields_otc - OTC_CSV_HEADER_FIELDS
# список полей (list) для "шапки" результирующего csv файла по категории ONE_TIME_CHARGE

fields_result - RESULT_CSV_HEADER_FIELDS
# список полей (list) для "шапки" итогового csv файла

CHUNK - CHUNK_SIZE_FOR_READING_BINARY_FILES
# размер порции для чтения бинарных файлов

# было
list_of_pdf_files = glob("pdf\\*.pdf")
# стало
PDF_FILE_SEARCH_TEMPLATE = "pdf\\*.pdf"
list_of_pdf_files = glob(PDF_FILE_SEARCH_TEMPLATE)
# шаблон поиска pdf файлов вынес в константу

REPORT_SECTIONS - REPORT_ROWS
# изначально это были секции отчета, но, фактически, каждая секция - это строка, поэтому так правильнее

WITH_NDS - COEFFICIENT_RATE_WITH_VAT
# коэффициент ставки с НДС - конкретизировал имя и вместо транслита НДС сделал перевод

# было
INPUT_FILES_PATH = "reports\\in\\" 
list_of_db_files = glob(f"{INPUT_FILES_PATH}db*.xlsx")
# стало
INPUT_FILES_PATH = "reports\\in\\" 
TEMPLATE_FOR_ACCOUNTS_RECEIVABLE_FILES = "db*.xlsx"
list_of_db_files = glob(f"{INPUT_FILES_PATH}{TEMPLATE_FOR_ACCOUNTS_RECEIVABLE_FILES}")
# каталог файлов был задан константой, а шаблон поиска файлов не задан - исправил это

list_of_planets - ALL_PLANETS_OF_SOLAR_SYSTEM
# планеты Солнечной системы

zodiac_signs - ALL_ZODIAC_SIGNS
# полный список знаков зодиака

# было
if not (list_of_5_strings[0].isdigit() and len(list_of_5_strings[0]) == 10):
# стало
PHONE_NUMBER_STANDART_LENGTH = 10
if not (list_of_5_strings[0].isdigit() and len(list_of_5_strings[0]) == PHONE_NUMBER_STANDART_LENGTH):
# "параметризация" программы

# было
ch_current.charge <= 25.0)
# ...
ch_previous.charge > 25.0)
# стало
BOUNDARY_FOR_CUTTING_OFF_PAYMENT_FOR_SILENCE = 25.0
# ...
ch_current.charge <= BOUNDARY_FOR_CUTTING_OFF_PAYMENT_FOR_SILENCE)
# ...
ch_previous.charge > BOUNDARY_FOR_CUTTING_OFF_PAYMENT_FOR_SILENCE)
# "параметризация" программы
