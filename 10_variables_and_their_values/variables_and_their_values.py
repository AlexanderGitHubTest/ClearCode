"""
Variables and their values.
"""

# правка 1
# было
def greet_user(update, bot):
    # ... много кода
    chat_id = update.message.chat_id
# стало
def greet_user(update, bot):
    # ... много кода
# присваивал значение переменной, чтобы сделать код менее громоздким
# переменная не используется: убрал её

# правка 2
# было
def button(update, bot):
    # ... код
    variant = query.data
    # ... много кода
    if variant == "none":
        # ... действия внутри if
    elif variant =="nice":
        # ... действия внутри elif
    # ... другие elif
# стало
def button(update, bot):
    # ... много кода
    selected_option = query.data
    if selected_option == "none":
        # ... действия внутри if
    elif selected_option =="nice":
        # ... действия внутри elif
    # ... другие elif
# присваивал значение переменной, чтобы было понятно назначение
# перенес присвоение значения ближе к использованию переменной,
# заодно переименовал её, чтобы более четко сущность была понятна

# правка 3
# было
def button(update, bot):
    # ... код
    chat_id = query.message.chat_id
    # ... много кода
    if selected_option == "none":
        # ... действия внутри if
    elif variant =="nice":
        # ... код
        bot.bot.send_animation(chat_id=chat_id, animation=open('gif/Uma Turman.gif', 'rb'))
    # ... много кода
# стало
def button(update, bot):
    # ... много кода
    selected_option = query.data
    chat_id = query.message.chat_id
    if selected_option == "none":
        # ... действия внутри if
    elif variant =="nice":
        # ... код
        bot.bot.send_animation(chat_id=chat_id, animation=open('gif/Uma Turman.gif', 'rb'))
    # ... много кода
# присваивал значение переменной, чтобы сделать код менее громоздким
# перенес присвоение значения ближе к использованию переменной
# хотя, возможно, стоит вообще избавиться от переменной

# правка 4
# было
def in_which_constellation_is_the_planet(update, bot):
    chat_id = update.message.chat_id
    # ... много кода
# стало
def in_which_constellation_is_the_planet(update, bot):
    # ... много кода
# присваивал значение переменной, чтобы сделать код менее громоздким
# переменная не используется: убрал её

# правка 5
# было
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()
# ... много кода: объявление объектов для всех таблиц
Base.metadata.create_all(engine)
# стало
Base = declarative_base()
# ... много кода: объявление объектов для всех таблиц
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(engine)
# создавал экземпляр базы SQLAlchemy до объявления объектов для таблиц
# перенес создание экземпляра базы SQLAlchemy ближе к его использованию

# правка 6
# было
FIELDS_RESULT_CSV = ["phone", "fee", "summa", "correction", "result"]
FILE_NAME_RESULT = "pdf\\result.csv"
report_result_out = session.query(
    Report.phone, 
    Report.fee,
    Report.summa,
    Report.correction,
    Report.result
    )
with open(FILE_NAME_RESULT, "w", encoding="1251") as f_result_out:
    writer = csv.DictWriter(f_result_out, FIELDS_RESULT_CSV, dialect="my_dialect")
    writer.writeheader()
    for result_out_row in report_result_out:
        result_out_row_dict = {
            "phone": result_out_row[0],
            "fee": formatting_float_for_csv(result_out_row[1]),
            "summa": formatting_float_for_csv(result_out_row[2]),
            "correction": formatting_float_for_csv(result_out_row[3]),
            "result": formatting_float_for_csv(result_out_row[4])
        }
        writer.writerow(result_out_row_dict)
# стало
FIELDS_RESULT_CSV = ["phone", "fee", "summa", "correction", "result"]
FILE_NAME_RESULT = "pdf\\result.csv"
with open(FILE_NAME_RESULT, "w", encoding="1251") as f_result_out:
    writer = csv.DictWriter(f_result_out, FIELDS_RESULT_CSV, dialect="my_dialect")
    writer.writeheader()
    report_result_out = session.query(Report.phone, 
                                      Report.fee,
                                      Report.summa,
                                      Report.correction,
                                      Report.result
                                     )
    for result_out_row in report_result_out:
        result_out_row_dict = {
            "phone": result_out_row[0],
            "fee": formatting_float_for_csv(result_out_row[1]),
            "summa": formatting_float_for_csv(result_out_row[2]),
            "correction": formatting_float_for_csv(result_out_row[3]),
            "result": formatting_float_for_csv(result_out_row[4])
        }
        writer.writerow(result_out_row_dict)
# присваивал значение переменной report_result_out, чтобы сделать код менее громоздким
# перенес присвоение значения ближе к использованию переменной

# правка 7
# было
pos_begin = stream_line_decode.find(b"TD\n(")
pos_end = None
if pos_begin != -1:
    while pos_begin != -1:
        pos_end = stream_line_decode.find(b")", pos_begin)
# стало
pos_begin = stream_line_decode.find(b"TD\n(")
while pos_begin != -1:
    pos_end = stream_line_decode.find(b")", pos_begin)
# pos_begin и pos_end  - границы текста в поле в таблице
# перед циклом инициализировал pos_end значением None,
# но в цикле этой переменной присваивается значение,
# поэтому инициализация перед циклом не нужна,
# заодно ненужный if убрал

# правка 8
# было
def stream_decoding(lines_of_stream):
    for stream_line in lines_of_stream:
        if stream_line["object_type"] == "stream_line":
            # ... много кода
            pos_begin = stream_line_decode.find(b"TD\n(")
            while pos_begin != -1:
                pos_end = stream_line_decode.find(b")", pos_begin)
                # ... много кода: изменяется pos_end
                yield # ...
                # ... код, изменяющий pos_begin
# стало
def stream_decoding(lines_of_stream):
    for stream_line in lines_of_stream:
        if stream_line["object_type"] == "stream_line":
            # ... много кода
            pos_begin = stream_line_decode.find(b"TD\n(")
            while pos_begin != -1:
                pos_end = stream_line_decode.find(b")", pos_begin)
                # ... много кода: изменяется pos_end
                yield # ...
                # ... код, изменяющий pos_begin
            pos_begin = -1
            pos_end = -1
# pos_begin и pos_end  - границы текста в поле в таблице
# после окончания цикла while присвоил "недопустимые" значения,
# так как цикл for будет продолжаться;
# по-хорошему, функцию stream_decoding нужно разбивать на несколько функций,
# так как она слишком много разного делает и разные уровни абстракции


# правка 9
# было
result_file = f"{OUTPUT_FILES_PATH}{RESULT_FILE}"
# ... много кода
wb.save(filename = result_file)
# стало
# ... много кода
wb.save(filename = f"{OUTPUT_FILES_PATH}{RESULT_FILE}")
# присваивал значение переменной result_file, чтобы сделать код менее громоздким
# переменная совпадает с константой (только регистр разный),
# да и без неё всё понятно; поэтому удалил переменную

# правка 10
# было
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
session = Session(bind=engine)
# ... много кода
def period_name(period):
    query = session.query(InitialData.period_name)
# стало
# ... много кода
session = Session(bind=create_engine(SQLALCHEMY_DATABASE_URI, echo=True))
def period_name(period):
    query = session.query(InitialData.period_name)
# переменная engine используется только в одном месте: убрал её
# перенёс инициализацию session ближе к её использованию

# правка 11
# было
def count_of_blocked_numbers_in_bill(period):
    period_for_report_end = add_months(period, 1)
    # ... много кода
    query = session.query(NumbersMovement.number, NumbersMovement.contract_name)
    query = query.join(subq_only_vk, 
            subq_only_vk.c.number == NumbersMovement.number)
    query = query.filter(
            NumbersMovement.report_period_to == period_for_report_end,
            not_(or_(NumbersMovement.contract_name.like("КО-%"),
            NumbersMovement.contract_name.like("СД-%"),
            NumbersMovement.contract_name.like("ЯЯ-%"),
            NumbersMovement.contract_name == None)))
    result_clients_query = query.all()
# стало
def count_of_blocked_numbers_in_bill(period):
    # ... много кода
    period_for_report_end = add_months(period, 1)
    result_clients_query = session.query(NumbersMovement.number, 
                                         NumbersMovement.contract_name
                                        ).join(subq_only_vk,
                                               subq_only_vk.c.number == NumbersMovement.number
                                              ).filter(NumbersMovement.report_period_to == period_for_report_end,
                                                       not_(or_(NumbersMovement.contract_name.like("КО-%"),
                                                       NumbersMovement.contract_name.like("СД-%"),
                                                       NumbersMovement.contract_name.like("ЯЯ-%"),
                                                       NumbersMovement.contract_name == None))
                                                      ).all(
                                                           )

# перенёс инициализацию period_for_report_end ближе к её использованию
# также убрал переменную query (временная, чтобы собрать запрос)

# правка 12
# было
def square_free_part(n):
    divisors = []
    if n == 1:
        return 1
    else:
        for i in range(2,n):
            if n % i == 0: divisors.append(i)
# стало
def square_free_part(n):
    if n == 1:
        return 1
    else:
        divisors = []
        for i in range(2,n):
            if n % i == 0: divisors.append(i)
# перенёс инициализацию переменной divisors ближе к её использованию

# правка 13
# было
def a(n):
    s = ''
    if n >= 4:
        n = n - 1 if n % 2 else n
        for i in range(n):
            if i == 0:
                s += " " * (n - 1) + "A" + " " * (n - 1) + "\n"
            elif i == int(n / 2):
                s += " " * (n - i - 1) + "A " * (n // 2 + 1) + " " * (n - i - 2) + "\n"
            else:
                s += " " * (n - i - 1) + "A" + " " * (i * 2 - 1) + "A" + " " * (n - i - 1) + "\n"
        s = s[:-1]
    return s
# стало
def a(n):
    if n < 4:
        return ''
    assert n >= 4, "The variable n here must be greater than or equal to 4"
    n = n - 1 if n % 2 else n
    for i in range(n):
        if i == 0:
            s += " " * (n - 1) + "A" + " " * (n - 1) + "\n"
        elif i == int(n / 2):
            s += " " * (n - i - 1) + "A " * (n // 2 + 1) + " " * (n - i - 2) + "\n"
        else:
            s += " " * (n - i - 1) + "A" + " " * (i * 2 - 1) + "A" + " " * (n - i - 1) + "\n"
    return s[:-1]
# ASCII art
# убрал ситуацию "for внутри if",
# после чего оказалось, что инициализация s вообще не нужна
# добавил assert на случай, если блок с n < 4 будет изменен

# правка 14
# было
import operator
from stack import Stack
def calculate_postfix_expression(expression):
    processed_operations = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv}
    stack1 = Stack()
    stack2 = Stack()
    for obj in expression.split()[::-1]:
        stack1.push(obj)
    while stack1.size() > 0:
        obj = stack1.pop()
        if obj.isdigit():
            stack2.push(obj)
        elif obj == '=':
            return stack2.pop()
        elif stack2.size() <= 1:
            raise Exception('Incorrect expression!')
        else:
            second_operand = int(stack2.pop())
            stack2.push(processed_operations[obj](int(stack2.pop()), second_operand))
    raise Exception('Empty expression or missing "="!')
# стало
import operator
from stack import Stack
def calculate_postfix_expression(expression):
    stack1 = Stack()
    stack2 = Stack()
    for obj in expression.split()[::-1]:
        stack1.push(obj)
    processed_operations = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv}
    while stack1.size() > 0:
        obj = stack1.pop()
        if obj.isdigit():
            stack2.push(obj)
        elif obj == '=':
            return stack2.pop()
        elif stack2.size() <= 1:
            raise Exception('Incorrect expression!')
        else:
            second_operand = int(stack2.pop())
            stack2.push(processed_operations[obj](int(stack2.pop()), second_operand))
    raise Exception('Empty expression or missing "="!')
# сделал инициализацию переменной processed_operations
# непосредственно перед циклом, где она используется

# правка 15
# было
report_even_pages_count = 0
# ... много кода
for page in pages:
    if pages.number % 2 == 0:
        report_even_pages_count += 1
    # ... много кода
pages.print_summary(report_even_pages_count, # ...
# стало
# ... много кода
report_even_pages_count = 0
for page in pages:
    if pages.number % 2 == 0:
        report_even_pages_count += 1
    # ... много кода
pages.print_summary(report_even_pages_count, # ...
report_even_pages_count = -1
# сделал инициализацию переменной report_even_pages_count 
# непосредственно перед циклом, где она используется;
# присвоил "недопустимое" значение после блока кода,
# где переменная используется
