import datetime as dt

# стр 6 , присваиване значений  функции __init__ разместить в той же последовательности, что её аргументы, то есть
# self.amount = amount, self.comment = comment, self.date = date
# стр 9 , убрать лишние скобки, разместить if/else в одну строку
class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

# Стр 30, написать "Record" c маленькой буквы. Большими буквами в пайтон называют классы, мы выводим не класс, а объект,
# который обозначается как обычная переменная
# нужно проверить, может ли record.amount  быть целым числом, перед тем как проводить вычисление. И привести к целому
# числу. Вводимые данные могут быть не всегда корректны
    def get_today_stats(self):
        today_stats = 0
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

# В конструкции if в Пайтон не должно быть скобок. К тому же, надо привести в такой вид
# 7 > (today - record.date).days >= 0 стр 41
    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


# стр 55 Название переменной должно быть осмысленным, а не просто x
# стр 59 Убрать ненужные скобки.
# стр 56 Бэкслеши для переносов не должны применяться.
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            return('Хватит есть!')


# Для расчётов в валюте надо использовать класс Decimal.
# стр 72. Имена аргументов должны начинаться с маленькой буквы. Разместить на одной строке
# стр 82 Исправить синтаксическую ошибку
# стр 91 elif заменить на else.
# стр 92 Бэкслеши для переносов не применяются.
class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

# Незачем переопределять метод, если в нём нет дополнительного функционала.
    def get_week_stats(self):
        super().get_week_stats()

