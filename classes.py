from collections import UserDict
from datetime import date
import re


class Field:
    _required = False
    _multi_field = False
    _value = None

    def __init__(self, value=None, required=False, multi_field=False) -> None:
        self._required = required
        self._multi_field = multi_field
        self._value = value


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(required=True)
        self.value = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        if value and type(value) == str:
            self._value = value
        else:
            self._value = "John Doe"


class Phone(Field):
    def __init__(self, value: str) -> None:
        super().__init__(multi_field=True)
        self.value = value

    def __sanitize_phone_number(self, phone):
        ptrn = re.compile(r"[+)(.\- ]")
        new_phone = re.sub(pattern=ptrn, repl="", string=phone)

        if (new_phone != phone):
            print(f'Phone number has been sanitized to "{new_phone}"')

        return new_phone

    @property
    def value(self) -> str | None:
        return self._value

    @value.setter
    def value(self, value: str):
        format_warning = '\n'.join([
            'Bad phone number format!',
            'The number:',
            '- should not have less than 3 digits',
            '- should not have more than 15 digits',
            '- may start from + and should contain only digits, parentheses, dots, giphens, spaces'
        ])

        if type(value) != str:
            try:
                value = str(value)
            except ValueError:
                print(format_warning)

        value = self.__sanitize_phone_number(value)

        uni_pattern = re.compile(r"^\d{3,15}$")

        if not re.match(pattern=uni_pattern, string=value):
            print(format_warning)

            self._value = None
        else:
            self._value = value


class Birthday(Field):
    def __init__(self, value: str) -> None:
        self.value = value

    @property
    def value(self) -> date | None:
        return self._value

    @value.setter
    def value(self, value: str):
        try:
            self._value = date.fromisoformat(value)
        except ValueError:
            print('Bad date format, should be "%Y-%m-%d" like "2000-01-01"')
            self._value = None


class Record:
    def __init__(self, name: Name, phone: Phone | None = None, birthday: Birthday | None = None) -> None:
        self.name = name
        self.phones = []
        self.birthday = birthday

        if phone:
            self.add_phone(phone)

    def days_to_birthday(self) -> int | None:
        if self.birthday and self.birthday.value is not None:
            current_date = date.today()

            current_year_bd = date(
                current_date.year,
                self.birthday.value.month,
                self.birthday.value.day
            )

            next_bd_year = current_date.year if current_year_bd >= current_date else current_date.year + 1

            next_birthday = date(
                next_bd_year,
                self.birthday.value.month,
                self.birthday.value.day
            )

            return (next_birthday - current_date).days

    def __find_phone(self, phone: Phone) -> int | None:
        for i, item in enumerate(self.phones):
            if item.value == phone.value:
                return i

    def add_phone(self, phone: Phone) -> None:
        if phone:
            self.phones.append(phone)

    def del_phone(self, phone: Phone) -> None:
        if (index := self.__find_phone(phone)) != None:
            self.phones.remove(self.phones[index])

    def edit_phone(self, current_value: Phone, new_value: Phone) -> None:
        if (index := self.__find_phone(current_value)) != None:
            self.phones[index].value = new_value.value


class AddressBook(UserDict):
    def __record_exists(self, record_key):
        return bool(self.data.get(record_key, None))

    def add_record(self, record: Record):
        if record and type(record) == Record:
            if self.__record_exists(record.name.value):
                print("The record exists!")
            else:
                self.data[record.name.value] = record
        else:
            print("Bad record type, should be Record()")

    def iterator(self, records_number=1):
        if records_number <= 0:
            records_number = 1
            print("Bad records number, set to default - 1")

        if records_number > len(self.data):
            records_number = len(self.data)

        ci = 0
        for _ in range(len(self.data)//records_number):
            yield dict(list(self.data.items())[ci:ci + records_number])
            ci += records_number
