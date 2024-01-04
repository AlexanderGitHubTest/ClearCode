"""
Lifetime of variables.
"""

# правка 1
# БЫЛО
def stream_decoding(lines_of_stream):
    # обрабатываю только строки с "object_type" == "stream_line",
    # остальные игнорирую
    for stream_line in lines_of_stream:
        if stream_line["object_type"] == "stream_line":
            if stream_line["flags"]["filter"]:
                # декодируем только, если встретился filter
                stream_line_decode = zlib.decompress(
                    stream_line["stream_line"]
                )
            else:
                stream_line_decode = stream_line["stream_line"]
            # позиция начала текста в потоке
            pos_begin = stream_line_decode.find(b"TD\n(")
            while pos_begin != -1:
                # скобка ')' - конец текста
                pos_end = stream_line_decode.find(b")", pos_begin)
                # но встречаются последовательности '\\)' -
                # такое является частью текста,
                # соответственно, проверяю найденное вхождение,
                # если оно часть текста, то двигаю pos_end
                pos_double_slash = stream_line_decode.find(
                    b"\\)",
                    pos_end-1,
                    pos_end+1
                )
                while pos_double_slash != -1:
                    pos_end = stream_line_decode.find(b")", pos_end + 1)
                    pos_double_slash = stream_line_decode.find(
                        b"\\)",
                        pos_end-1,
                        pos_end+1
                    )
                yield stream_line_decode[pos_begin+4: pos_end].replace(
                    b"\\)",
                    b")"
                    ).replace(b"\\(", b"(").decode("1251")
                pos_begin = stream_line_decode.find(
                    b"TD\n(",
                    pos_begin + 1
                    )
# СТАЛО
def stream_decoding(lines_of_stream):
    # обрабатываю только строки с "object_type" == "stream_line",
    # остальные игнорирую
    for stream_line in lines_of_stream:
        if (    stream_line["object_type"] == "stream_line" 
            and stream_line["flags"]["filter"]
           ):
            # декодируем только, если встретился filter
            yield zlib.decompress(stream_line["stream_line"])
        elif stream_line["object_type"] == "stream_line":
            yield stream_line["stream_line"]
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
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# переменные pos_begin и pos_end имеют слишком большое окно "уязвимости",
# более того, они "видны" также и на бОльшем уровне абстракции, чем нужно;
# разбил функцию на две, чтобы сделать правильные уровни абстракции и 
# уменьшить окно "уязвимости";
# кроме того pos_double_slash просто является условием для while:
# убрал её, а вычисления перенёс в условие

# правка 2
# БЫЛО 
# основной модуль
# ... много кода
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "for_report.db")
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()
class Agprior(Base):
    __tablename__ = "agprior"
    id = Column(Integer, primary_key=True)
# ... всего объявляется 5 классов, соответствующих таблицам (исходные, результат и и временные)
Base.metadata.create_all(engine)
# ... много кода
# СТАЛО
# -= отдельный модуль model.py - начало =-
# ... необходимые импорты
Base = declarative_base()
class Agprior(Base):
    __tablename__ = "agprior"
    id = Column(Integer, primary_key=True)
# ... всего объявляется 5 классов, соответствующих таблицам (исходные, результат и и временные)
# -= отдельный модуль model.py - конец =-
# основной модуль
# добавлен импорт Base и классов из model.py
# ... много кода
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "for_report.db")
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(engine)
# ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# Вынес в отдельный модуль объявление классов и импортирую их уже оттуда (плюс Base)

# правка 3
# БЫЛО 
# ... много кода
session = Session(bind=engine)
session.query(Agprior).delete()
session.query(AgpriorGrp).delete()
session.query(OneCharge).delete()
session.query(OneChargeGrp).delete()
session.query(Report).delete()
session.commit()
# ... много кода
# СТАЛО
# ... много кода
def clear_tables(session):
    session.query(Agprior).delete()
    session.query(AgpriorGrp).delete()
    session.query(OneCharge).delete()
    session.query(OneChargeGrp).delete()
    session.query(Report).delete()
    session.commit()
# ... много кода
session = Session(bind=engine)
clear_tables(session)
# ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# Вынес в отдельную функцию очистку таблиц, чтобы уменьшить окна "уязвимости" переменных в основном теле программы

# правка 4
# БЫЛО 
# ... много кода
fields = ["phone", "from_date", "to_date", "service_name", "fee", "type"]
FILE_NAME_AGPRIOR = "pdf\\agprior.csv"
csv.register_dialect("my_dialect", delimiter=";", lineterminator="\n")
with open(FILE_NAME_AGPRIOR, "r", encoding="1251") as f_in:
    reader = csv.DictReader(f_in, fields, dialect="my_dialect")
    for i, line_in_reader in enumerate(reader):
        if i == 0:
            continue
        string = Agprior(
            phone=line_in_reader["phone"],
            from_date=str_to_date(line_in_reader["from_date"]),
            to_date=str_to_date(line_in_reader["to_date"]),
            service_name=line_in_reader["service_name"],
            fee=Decimal(line_in_reader["fee"].replace(",", ".")) , 
            type=line_in_reader["type"]           
        )
        session.add(string)
    session.commit()   
fields_otc = ["phone", "description", "charge", "quantity", "summa", "type"]
FILE_NAME_ONE_TIME_CHARGE = "pdf\\onecharge.csv"
with open(FILE_NAME_ONE_TIME_CHARGE, "r", encoding="1251") as f_otc_in:
    reader = csv.DictReader(f_otc_in, fields_otc, dialect="my_dialect")
    for i, line_in_reader in enumerate(reader):
        if i == 0:
            continue
        string = OneCharge(
            phone=line_in_reader["phone"],
            description=line_in_reader["description"],
            charge=Decimal(line_in_reader["charge"].replace(",", ".")),
            quantity=int(line_in_reader["quantity"]),
            summa=Decimal(line_in_reader["summa"].replace(",", ".")) , 
            type=line_in_reader["type"]           
        )
        session.add(string)
    session.commit()
# СТАЛО
# ... много кода
AGPRIOR_CSV_HEADER_FIELDS = [{"name": "phone", "type": "str"},
                             {"name": "from_date", "type": "date"}, 
                             {"name": "to_date", "type": "date"}, 
                             {"name": "service_name", "type": "str"}, 
                             {"name": "fee", "type": "decimal"}, 
                             {"name": "type", "type": "str"}
                            ]
OTC_CSV_HEADER_FIELDS = [{"name": "phone", "type": "str"},
                         {"name": "description", "type": "str"},
                         {"name": "charge", "type": "decimal"}, 
                         {"name": "quantity", "type": "int"}, 
                         {"name": "summa", "type": "decimal"}, 
                         {"name": "type", "type": "str"}
                        ]
FILE_NAME_AGPRIOR = "pdf\\agprior.csv"
FILE_NAME_OTC = "pdf\\onecharge.csv"
csv.register_dialect("my_dialect", delimiter=";", lineterminator="\n")
# ... много кода
def download_from_csv_to_table(session, csv_header_fields, csv_file_name, class_table):
    fields_list = [element["name"] for element in csv_header_fields]
    with open(csv_file_name, "r", encoding="1251") as f_in:
        reader = csv.DictReader(f_in, fields_list, dialect="my_dialect")
        for line_in_reader in reader[1:]:
            processed_string = []
            for field in csv_header_fields:
                if field["type"] == "int":
                    processed_string.append(int(line_in_reader[field["name"]]))
                    continue
                if field["type"] == "decimal":
                    processed_string.append(Decimal(line_in_reader[field["name"]].replace(",", ".")))
                    continue
                if field["type"] == "date":
                    processed_string.append(str_to_date(line_in_reader[field["name"]]))
                    continue
                processed_string.append(line_in_reader[field["name"]])
            string = class_table(*processed_string)
            session.add(string)
        session.commit()   
# ... много кода
download_from_csv_to_table(session, AGPRIOR_CSV_HEADER_FIELDS, FILE_NAME_AGPRIOR, Agprior)
download_from_csv_to_table(session, OTC_CSV_HEADER_FIELDS, FILE_NAME_OTC, OneCharge)
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# Вынес в отдельную функцию загрузку таблиц из csv, чтобы уменьшить окна "уязвимости" переменных в основном теле программы

# правка 5
# БЫЛО 
# ... много кода
sql_result_out = session.query(
    Report.phone, 
    Report.fee,
    Report.summa,
    Report.correction,
    Report.result
    )
fields_result = ["phone", "fee", "summa", "correction", "result"]
FILE_NAME_RESULT = "pdf\\result.csv"
with open(FILE_NAME_RESULT, "w", encoding="1251") as f_result_out:
    writer = csv.DictWriter(f_result_out, fields_result, dialect="my_dialect")
    writer.writeheader()
    for tuple_for_out in sql_result_out:
        dict_for_out = {
            "phone": tuple_for_out[0],
            "fee": formatting_float_for_csv(tuple_for_out[1]),
            "summa": formatting_float_for_csv(tuple_for_out[2]),
            "correction": formatting_float_for_csv(tuple_for_out[3]),
            "result": formatting_float_for_csv(tuple_for_out[4])
        }
        writer.writerow(dict_for_out)
# СТАЛО
# ... много кода
RESULT_CSV_HEADER_FIELDS = [{"name": "phone", "type": "str"},
                             {"name": "fee", "type": "float"}, 
                             {"name": "summa", "type": "float"}, 
                             {"name": "correction", "type": "float"}, 
                             {"name": "result", "type": "float"} 
                            ]
FILE_NAME_RESULT = "pdf\\result.csv"
# ... много кода
def upload_from_table_to_csv(session, csv_header_fields, csv_file_name, sql_for_output):
    fields_result = [element["name"] for element in csv_header_fields]
    with open(csv_file_name, "w", encoding="1251") as f_result_out:
        writer = csv.DictWriter(f_result_out, fields_result, dialect="my_dialect")
        writer.writeheader()
        for tuple_for_out in sql_for_output:
            for line_in_reader in reader[1:]:
                processed_dict = {}
                for i, field in enumerate(csv_header_fields):
                    if field["type"] == "float":
                        processed_dict[field["name"]] = formatting_float_for_csv(tuple_for_out[i])
                        continue
                    processed_dict["name"] = tuple_for_out[i]
            writer.writerow(processed_dict)
# ... много кода
sql_result_out = session.query(
    Report.phone, 
    Report.fee,
    Report.summa,
    Report.correction,
    Report.result
    )
upload_from_table_to_csv(session, RESULT_CSV_HEADER_FIELDS, FILE_NAME_RESULT, sql_result_out)
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# Вынес в отдельную функцию выгрузку таблицы в csv, чтобы уменьшить окна "уязвимости" переменных в основном теле программы

# правка 6
# БЫЛО 
# ... много кода
sql_groupping_agprior = session.query(Agprior.phone, func.sum(Agprior.fee)).group_by(Agprior.phone)
for row in sql_groupping_agprior:
    string = AgpriorGrp(
        phone=row[0],
        fee=row[1]
    )
    session.add(string)
session.commit()
sql_groupping_onecharge = session.query(OneCharge.phone, func.sum(OneCharge.summa)).group_by(OneCharge.phone)
for row in sql_groupping_onecharge:
    string = OneChargeGrp(
        phone=row[0],
        summa=row[1]
    )
    session.add(string)
session.commit()
sql_result = session.query(AgpriorGrp.phone, 
    AgpriorGrp.fee, 
    OneChargeGrp.summa).outerjoin(OneChargeGrp, AgpriorGrp.phone == OneChargeGrp.phone)
for row in sql_result:
    string = Report(
        phone=row[0],
        fee=row[1],
        summa=row[2],
        correction=calculate_correction(row[1], row[2]),
        result=calculate_result(row[1], row[2]) 
    )
    session.add(string)
session.commit()
# ... много кода
# СТАЛО
# ... много кода
def get_resulting_table(session):
    sql_groupping_agprior = session.query(Agprior.phone, func.sum(Agprior.fee)).group_by(Agprior.phone)
    for row in sql_groupping_agprior:
        string = AgpriorGrp(
            phone=row[0],
            fee=row[1]
        )
        session.add(string)
    session.commit()
    sql_groupping_onecharge = session.query(OneCharge.phone, func.sum(OneCharge.summa)).group_by(OneCharge.phone)
    for row in sql_groupping_onecharge:
        string = OneChargeGrp(
            phone=row[0],
            summa=row[1]
        )
        session.add(string)
    session.commit()
    sql_result = session.query(AgpriorGrp.phone, 
        AgpriorGrp.fee, 
        OneChargeGrp.summa).outerjoin(OneChargeGrp, AgpriorGrp.phone == OneChargeGrp.phone)
    for row in sql_result:
        string = Report(
            phone=row[0],
            fee=row[1],
            summa=row[2],
            correction=calculate_correction(row[1], row[2]),
            result=calculate_result(row[1], row[2]) 
        )
        session.add(string)
    session.commit()
# ... много кода
get_resulting_table(session)
# ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# Вынес в отдельную функцию группировки и создание результирующей таблицы чтобы 
# минимизировать область видимости для части переменных, а по переменным в основном теле программы 
# уменьшить окна "уязвимости"

# правка 7
# БЫЛО 
# ... много кода
list_of_db = glob(f"{INPUT_FILES_PATH}db*.xlsx")
for db_file in list_of_db:
    date_from_file_name = str_to_date(db_file[-15:-5])
    wb = load_workbook(filename=db_file, read_only=True)
    ws = wb["Sheet1"]
    for i, row in enumerate(ws.rows):
        if i == 0:
            continue
        string = DebitArrears(
            report_date = date_from_file_name,
            contract_name = row[0].value,
            client_name = row[1].value,
            balance = row[2].value,
            vip_status = row[3].value,
            client_type = row[4].value,
            postponement = row[5].value,
            active_numbers_count = row[6].value,
            blocked_numbers_count = row[7].value
        )
        session.add(string)
    session.commit()
    wb.close()
# ... много кода
# СТАЛО
# ... много кода
def upload_files_with_accounts_receivable(file_name_template, class_for_table):
    list_of_db = glob(f"{INPUT_FILES_PATH}{file_name_template}")
    for db_file in list_of_db:
        date_from_file_name = str_to_date(db_file[-15:-5])
        wb = load_workbook(filename=db_file, read_only=True)
        ws = wb["Sheet1"]
        for i, row in enumerate(ws.rows):
            if i == 0:
                continue
            string = class_for_table(
                report_date = date_from_file_name,
                contract_name = row[0].value,
                client_name = row[1].value,
                balance = row[2].value,
                vip_status = row[3].value,
                client_type = row[4].value,
                postponement = row[5].value,
                active_numbers_count = row[6].value,
                blocked_numbers_count = row[7].value
            )
            session.add(string)
        session.commit()
        wb.close()
upload_files_with_accounts_receivable("db*.xlsx", DebitArrears):
# ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# данный блок загружает данные из xlsx файла в таблицу базы sqlite;
# в блоке много переменных, которые используются только в нём
# вынес блок в функцию, чтобы локализовать переменные

# правка 8
# БЫЛО 
# ... много кода
list_of_mv = glob(f"{INPUT_FILES_PATH}mv*.xlsx")
for mv_file in list_of_mv:
    date_period_from = str_to_date(mv_file[-26:-16])
    date_period_to = str_to_date(mv_file[-15:-5])
    wb = load_workbook(filename=mv_file, read_only=True)
    ws = wb["Sheet1"]
    for i, row in enumerate(ws.rows):
        if i == 0:
            continue
        string = NumbersMovement(
            report_period_from = date_period_from,
            report_period_to = date_period_to,
            number = row[0].value,
            contract_name = row[1].value,
            status = row[2].value,
            status_date = row[3].value
        )
        session.add(string)
    session.commit()
    wb.close()
# ... много кода
# СТАЛО
# ... много кода
def upload_files_with_changing_ctn_statuses(file_name_template, class_for_table):
    list_of_mv = glob(f"{INPUT_FILES_PATH}{file_name_template}")
    for mv_file in list_of_mv:
        date_period_from = str_to_date(mv_file[-26:-16])
        date_period_to = str_to_date(mv_file[-15:-5])
        wb = load_workbook(filename=mv_file, read_only=True)
        ws = wb["Sheet1"]
        for i, row in enumerate(ws.rows):
            if i == 0:
                continue
            string = class_for_table(
                report_period_from = date_period_from,
                report_period_to = date_period_to,
                number = row[0].value,
                contract_name = row[1].value,
                status = row[2].value,
                status_date = row[3].value
            )
            session.add(string)
        session.commit()
        wb.close()
upload_files_with_changing_ctn_statuses("mv*.xlsx", NumbersMovement):
# ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# данный блок загружает данные из xlsx файла в таблицу базы sqlite;
# в блоке много переменных, которые используются только в нём
# вынес блок в функцию, чтобы локализовать переменные

# правка 9
# БЫЛО 
# ... много кода
initial_file = f"{INPUT_FILES_PATH}initial_data.xlsx"
wb = load_workbook(filename=initial_file, read_only=True)
ws = wb["Sheet1"]
for i, row in enumerate(ws.rows):
    if i == 0:
        continue
    string = InitialData(
        period_name = row[0].value,
        active_credit_numbers_from_bill = row[1].value,
        active_avans_numbers_from_bill = row[2].value,
        transfer_mnp_numbers_recalculated = row[3].value,
        transfer_mnp_numbers_non_recalculated = row[4].value,
        ekomobile_bill = row[5].value,
        vimpelcom_bill_with_agprior = row[6].value,
        agprior = row[7].value,
        vimpelcom_bill_without_agprior = row[8].value,
        vimpelcom_pay = row[9].value,
        sberbank_pay = row[10].value
    )
    session.add(string)
session.commit()
# ... много кода
# СТАЛО
# ... много кода
def upload_files_with_initial_data(file_name, class_for_table):
    wb = load_workbook(filename=f"{INPUT_FILES_PATH}{file_name}", 
                       read_only=True
                      )
    for i, row in enumerate(wb["Sheet1"].rows[1:]):
        string = class_for_table(
            period_name = row[0].value,
            active_credit_numbers_from_bill = row[1].value,
            active_avans_numbers_from_bill = row[2].value,
            transfer_mnp_numbers_recalculated = row[3].value,
            transfer_mnp_numbers_non_recalculated = row[4].value,
            ekomobile_bill = row[5].value,
            vimpelcom_bill_with_agprior = row[6].value,
            agprior = row[7].value,
            vimpelcom_bill_without_agprior = row[8].value,
            vimpelcom_pay = row[9].value,
            sberbank_pay = row[10].value
        )
        session.add(string)
    session.commit()
upload_files_with_initial_data("initial_data.xlsx", InitialData):
# ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# данный блок загружает данные из xlsx файла в таблицу базы sqlite;
# в блоке много переменных, которые используются только в нём
# вынес блок в функцию, чтобы локализовать переменные

# правка 10
# БЫЛО 
# ... много кода
QUERY_TEXT = text(
    "INSERT INTO charges (period_date, number, charge) "
    "SELECT charges_temp.period_date, charges_temp.number, sum(charges_temp.charge) as sum_charge "
    "FROM charges_temp "
    "GROUP BY charges_temp.period_date, charges_temp.number "
    "HAVING sum(charges_temp.charge) <> 0")
list_of_bill_c = glob(f"{INPUT_FILES_PATH}bill_c*.xls*")
for bill_c_file in list_of_bill_c:
    session.query(ChargesTemp).delete()
    session.commit()    
    date_from_file_name = str_to_date(bill_c_file[-15:-5])
    wb = load_workbook(filename=bill_c_file, read_only=True)
    ws = wb[wb.sheetnames[0]]
    ws_max_row = ws.max_row
    for i, row in enumerate(ws.rows):
        if i == 0:
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
            if row[15].value == "Итого с налогами": # столбец P
                charge_row = 15
            elif row[17].value == "Итого с налогами": # столбец R
                charge_row = 17
            elif row[20].value == "Итого с налогами": # столбец U
                charge_row = 20            
            elif row[21].value == "Итого с налогами": # столбец V
                charge_row = 21
            elif row[22].value == "Итого с налогами": # столбец W
                charge_row = 22
            elif row[23].value == "Итого с налогами": # столбец X
                charge_row = 23
            elif row[17].value == "Итого с налогами\nsum_and_tax\n[#1944]": # столбец R
                charge_row = 17
            elif row[18].value == "Итого с налогами\nsum_and_tax\n[#1944]": # столбец S
                charge_row = 18
            elif row[18].value == "Итого с налогами": # столбец S
                charge_row = 18
            else:
                raise "Ошибочный формат файла с начислениями по кредитным!"
            continue
        string = ChargesTemp(
            period_date = date_from_file_name,
            number = row[number_row].value,
            charge = row[charge_row].value,
        )
        session.add(string)
    session.commit()
    wb.close()
    bill_a_file = bill_c_file.replace("bill_c", "bill_a")
    date_from_file_name = str_to_date(bill_a_file[-15:-5])
    wb = load_workbook(filename=bill_a_file, read_only=True)
    ws = wb[wb.sheetnames[0]]
    for i, row in enumerate(ws.rows):
        if i == 0:
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
    with engine.connect() as connection:
        result = connection.execute(QUERY_TEXT)
# ... много кода
# СТАЛО
# ... много кода
def upload_files_with_accruals_by_ctns(file_name_template, class_for_table):
    QUERY_TEXT = text(
        "INSERT INTO charges (period_date, number, charge) "
        "SELECT charges_temp.period_date, charges_temp.number, sum(charges_temp.charge) as sum_charge "
        "FROM charges_temp "
        "GROUP BY charges_temp.period_date, charges_temp.number "
        "HAVING sum(charges_temp.charge) <> 0")
    list_of_bill_c = glob(f"{INPUT_FILES_PATH}{file_name_template}")
    for bill_c_file in list_of_bill_c:
        session.query(class_for_table).delete()
        session.commit()    
        date_from_file_name = str_to_date(bill_c_file[-15:-5])
        wb = load_workbook(filename=bill_c_file, read_only=True)
        ws = wb[wb.sheetnames[0]]
        ws_max_row = ws.max_row
        for i, row in enumerate(ws.rows):
            if i == 0:
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
                if row[15].value == "Итого с налогами": # столбец P
                    charge_row = 15
                elif row[17].value == "Итого с налогами": # столбец R
                    charge_row = 17
                elif row[20].value == "Итого с налогами": # столбец U
                    charge_row = 20            
                elif row[21].value == "Итого с налогами": # столбец V
                    charge_row = 21
                elif row[22].value == "Итого с налогами": # столбец W
                    charge_row = 22
                elif row[23].value == "Итого с налогами": # столбец X
                    charge_row = 23
                elif row[17].value == "Итого с налогами\nsum_and_tax\n[#1944]": # столбец R
                    charge_row = 17
                elif row[18].value == "Итого с налогами\nsum_and_tax\n[#1944]": # столбец S
                    charge_row = 18
                elif row[18].value == "Итого с налогами": # столбец S
                    charge_row = 18
                else:
                    raise "Ошибочный формат файла с начислениями по кредитным!"
                continue
            string = class_for_table(
                period_date = date_from_file_name,
                number = row[number_row].value,
                charge = row[charge_row].value,
            )
            session.add(string)
        session.commit()
        wb.close()
        bill_a_file = bill_c_file.replace("bill_c", "bill_a")
        date_from_file_name = str_to_date(bill_a_file[-15:-5])
        wb = load_workbook(filename=bill_a_file, read_only=True)
        ws = wb[wb.sheetnames[0]]
        for i, row in enumerate(ws.rows):
            if i == 0:
                if row[2].value == "score_sum": # столбец С
                    charge_row = 2
                elif row[2].value == "Сумма списаний": # столбец С
                    charge_row = 2
                elif row[3].value == "Общий итог": # столбец E
                    charge_row = 3
                elif row[4].value == "Общий итог": # столбец F
                    charge_row = 4
                elif row[6].value == "Общий итог": # столбец G
                    charge_row = 6
                else:
                    raise "Ошибочный формат файла с начислениями по авансовым!"
                continue
            if (   isinstance(row[0].value, int)
                or (    isinstance(row[0].value, str) 
                    and row[0].value.isnumeric()
                   )
               ):   
                string = class_for_table(
                    period_date = date_from_file_name,
                    number = row[0].value,
                    charge = -row[charge_row].value,
                )
                session.add(string)
        session.commit()
        wb.close()
        with engine.connect() as connection:
            result = connection.execute(QUERY_TEXT)
upload_files_with_accruals_by_ctns("bill_c*.xls*", ChargesTemp):
# ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# данный блок загружает данные из xls* файлов во временную таблицу базы sqlite;
# затем запросом заполняет рабочую таблицу базы sqlite;
# в блоке много переменных, которые используются только в нём
# вынес блок в функцию, чтобы локализовать переменные

# правка 11
# БЫЛО 
QUERY_TEXT = text(
    "INSERT INTO charges_vk (period_date, number, ban, charge) "
    "SELECT charges_vk_temp.period_date, charges_vk_temp.number, min(charges_vk_temp.ban) as min_ban, sum(charges_vk_temp.charge) as sum_charge "
    "FROM charges_vk_temp "
    "GROUP BY charges_vk_temp.period_date, charges_vk_temp.number ")
csv.register_dialect("my_dialect", delimiter=";", lineterminator="\n")
list_of_billvk = glob(f"{INPUT_FILES_PATH}billvk*.csv")
for billvk_file in list_of_billvk:
    session.query(ChargesVkTemp).delete()
    session.commit()    
    date_from_file_name = str_to_date(billvk_file[-14:-4])
    with open(billvk_file,"r", encoding="1251") as f:    
        reader = csv.reader(f, dialect= "my_dialect")
        for i, line in enumerate(reader):
            if i == 0:
                continue
            number_lstrip_0 = line[0].lstrip("0")
            if number_lstrip_0.isnumeric() and len(number_lstrip_0) == 10:
                string = ChargesVkTemp(
                    period_date = date_from_file_name,
                    number = number_lstrip_0,
                    ban = line[1],
                    ben = line[2],
                    charge = float(line[28].replace(",", "."))
                )
                session.add(string)
        session.commit()  
    with engine.connect() as connection:
        result = connection.execute(QUERY_TEXT)
# СТАЛО
# ... много кода
def upload_files_with_accruals_by_ctns_from_Vimpelcom(file_name_template, class_for_table):
    QUERY_TEXT = text(
        "INSERT INTO charges_vk (period_date, number, ban, charge) "
        "SELECT charges_vk_temp.period_date, charges_vk_temp.number, min(charges_vk_temp.ban) as min_ban, sum(charges_vk_temp.charge) as sum_charge "
        "FROM charges_vk_temp "
        "GROUP BY charges_vk_temp.period_date, charges_vk_temp.number ")
    csv.register_dialect("my_dialect", delimiter=";", lineterminator="\n")
    list_of_billvk = glob(f"{INPUT_FILES_PATH}{file_name_template}")
    for billvk_file in list_of_billvk:
        session.query(class_for_table).delete()
        session.commit()    
        date_from_file_name = str_to_date(billvk_file[-14:-4])
        with open(billvk_file,"r", encoding="1251") as f:    
            reader = csv.reader(f, dialect= "my_dialect")
            for i, line in enumerate(reader):
                if i == 0:
                    continue
                number_lstrip_0 = line[0].lstrip("0")
                if number_lstrip_0.isnumeric() and len(number_lstrip_0) == 10:
                    string = class_for_table(
                        period_date = date_from_file_name,
                        number = number_lstrip_0,
                        ban = line[1],
                        ben = line[2],
                        charge = float(line[28].replace(",", "."))
                    )
                    session.add(string)
            session.commit()  
        with engine.connect() as connection:
            result = connection.execute(QUERY_TEXT)
upload_files_with_accruals_by_ctns_from_Vimpelcom("billvk*.csv", ChargesVkTemp):
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# данный блок загружает данные из csv файла в таблицу базы sqlite;
# в блоке много переменных, которые используются только в нём
# вынес блок в функцию, чтобы локализовать переменные

# правка 12
# БЫЛО 
if __name__ == "__main__":
    # ... много кода
    ws.column_dimensions[utils.cell.get_column_letter(1)].width = 88
    for col in range(len_period_names):
        ws.column_dimensions[utils.cell.get_column_letter(col+2)].width = 14
    for col in range(len_period_names):
        ws[
            f"{utils.cell.get_column_letter(col+2)}{1}"
        ].number_format = "mmmm yyyy;@"
    max_row = max([iter["row_for_excel"] 
        for iter in REPORT_SECTIONS
        if iter["output_to_report"]])
    thins = Side(border_style="thin", color="000000")
    for col in range(len_period_names + 1):
        for row in range(max_row):
            ws[
                f"{utils.cell.get_column_letter(col + 1)}{row+1}"
                ].border = Border(
                    top=thins, 
                    bottom=thins, 
                    left=thins, 
                    right=thins)
    ws.freeze_panes = "B2"
# СТАЛО
def formatting_excel_sheet(ws, len_period_names):
    ws.column_dimensions[utils.cell.get_column_letter(1)].width = 88
    for col in range(len_period_names):
        ws.column_dimensions[utils.cell.get_column_letter(col+2)].width = 14
    for col in range(len_period_names):
        ws[
            f"{utils.cell.get_column_letter(col+2)}{1}"
        ].number_format = "mmmm yyyy;@"
    max_row = max([iter["row_for_excel"] 
        for iter in REPORT_SECTIONS
        if iter["output_to_report"]])
    thins = Side(border_style="thin", color="000000")
    for col in range(len_period_names + 1):
        for row in range(max_row):
            ws[
                f"{utils.cell.get_column_letter(col + 1)}{row+1}"
                ].border = Border(
                    top=thins, 
                    bottom=thins, 
                    left=thins, 
                    right=thins)
    ws.freeze_panes = "B2"
if __name__ == "__main__":
    # ... много кода
    formatting_excel_sheet(ws, len_period_names)
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# основной модуль создает сводный отчет в формате excel и форматирует его;
# вынес форматирование в отдельную функцию

# правка 13
# БЫЛО 
if __name__ == "__main__":
    # ... код
    if EXTENDED_RESULT:
        list_of_xlsx = glob(f"{QUERY_OUTPUT_FILES_PATH}*.xlsx")
        for file_for_delete in list_of_xlsx:
            os.remove(file_for_delete)
    # ... много кода
# СТАЛО
def clear_folder_for_additional_files()
    list_of_xlsx = glob(f"{QUERY_OUTPUT_FILES_PATH}*.xlsx")
    for file_for_delete in list_of_xlsx:
        os.remove(file_for_delete)
if __name__ == "__main__":
    # ... код
    if EXTENDED_RESULT:
        clear_folder_for_additional_files()
    # ... много кода
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# очистку папки для выгрузки дополнительных файлов
# вынес в отдельную функцию, чтобы локализовать переменные

# правка 14
# БЫЛО
if __name__ == "__main__":
    # ... много кода
                # Установим правильное форматирование ячеек
                # для строк c "money_format" == True
                # с 2 знаками после запятой и разделение троек разрядов пробелами
                # Нужный формат BUILTIN_FORMATS[4] (выглядит как '#,##0.00'))
                # В русском экселе будет виден как '# ##0,00'
                if section["money_format"]:
                    ws[
                        f"{utils.cell.get_column_letter(col+2)}{section['row_for_excel']}"
                    ].number_format = BUILTIN_FORMATS[4]
# ... много кода
# СТАЛО
def set_monetary_formatting(worksheet, column, row):
    """
    Установка правильного форматирования ячеек
    для строк c 'money_format':
    с 2 знаками после запятой и разделение троек разрядов пробелами.
    Нужный формат BUILTIN_FORMATS[4] (выглядит как '#,##0.00'))
    В русском экселе будет виден как '# ##0,00'
    """
    worksheet[
       f"{utils.cell.get_column_letter(column)}{row}"
      ].number_format = BUILTIN_FORMATS[4]
if __name__ == "__main__":
    # ... много кода
                if section["money_format"]:
                    set_monetary_formatting(ws, col+2, section['row_for_excel'])
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# для переменных основного цикла обработки уменьшил окно "уязвимости"
# (вынес часть кода основного цикла в функцию)

# правка 15
# БЫЛО
# ... много кода
def in_which_constellation_is_the_planet(update, bot):
    chat_id = update.message.chat_id
    text_list = update.message.text.split(" ")
    if len(text_list)<2:
        update.message.reply_text("Ошибка в названии планеты. Попробуй еще раз. Нужно набрать /planet и название планеты по-английски с большой буквы (например, '/planet Mars').")
        return
    text = text_list[1]
    current_date = date.today()
    if text == "Mercury":
        planet = ephem.Mercury(current_date)
    elif text == "Venus":
        planet = ephem.Venus(current_date)
    elif text == "Earth":
        planet = ephem.Earth(current_date)
    elif text == "Mars":
        planet = ephem.Mars(current_date)
    elif text == "Jupiter":
        planet = ephem.Jupiter(current_date)
    elif text == "Saturn":
        planet = ephem.Saturn(current_date)
    elif text == "Uranus":
        planet = ephem.Uranus(current_date)
    elif text == "Neptune":
        planet = ephem.Neptune(current_date)
    else:
        update.message.reply_text("Ошибка в названии планеты. Попробуй еще раз. Нужно набрать /planet и название планеты по-английски с большой буквы (например, '/planet Mars').")
        return
    const = ephem.constellation(planet)[1]    
    update.message.reply_text(f"Планета {text} сегодня в знаке зодиака: '{zodiac_signs[const]}'")
# ... много кода
# СТАЛО
# ... много кода
PLANETS = {"Mercury": ephem.Mercury,
           "Venus":   ephem.Venus,
           "Earth":   ephem.Earth,
           "Mars":    ephem.Mars,
           "Jupiter": ephem.Jupiter,
           "Saturn":  ephem.Saturn,
           "Uranus":  ephem.Uranus,
           "Neptune": ephem.Neptune}
# ... много кода
def in_which_constellation_is_the_planet(update, bot):
    text_list = update.message.text.split(" ")
    if len(text_list)<2:
        update.message.reply_text(  "Ошибка в названии планеты. Попробуй еще раз. Нужно набрать /planet и название" 
                                  + " планеты по-английски с большой буквы (например, '/planet Mars')."
                                 )
        return
    if PLANETS.get(text_list[1]) == None:
        update.message.reply_text(  "Ошибка в названии планеты. Попробуй еще раз. Нужно набрать /planet и название"
                                  + " планеты по-английски с большой буквы (например, '/planet Mars')."
                                 )
        return
    planet = PLANETS[text_list[1]](date.today())
    const = ephem.constellation(planet)[1]    
    update.message.reply_text(f"Планета {text} сегодня в знаке зодиака: '{zodiac_signs[const]}'")
# ОПИСАНИЕ И ЧТО ДЕЛАЛ
# сделал константу, чтобы убрать длинный if и сократить тем самым окно "уязвимости"
# попутно убрал лишние переменные
