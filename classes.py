from collections import UserDict


class Field:
    _required = False
    _multi_field = False
    value = None

    def __init__(self, value=None, required=False, multi_field=False) -> None:
        self._required = required
        self._multi_field = multi_field
        self.value = value


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value=value, required=True)


class Phone(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value=value, multi_field=True)


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    def __find_phone(self, phone: str) -> int|None:
        for i, item in  enumerate(self.phones):
            if item.value == phone:
                return i
            
    def add_phone(self, phone: str) -> None:
        if phone:
            self.phones.append(Phone(phone))

    def del_phone(self, phone: str) -> None:
        if (index := self.__find_phone(phone)) != None:
            self.phones.remove(self.phones[index])

    def edit_phone(self, current_value: str, new_value: str) -> None:
        if (index := self.__find_phone(current_value)) != None:
            self.phones[index].value = new_value


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record and type(record) == Record:
            self.data[record.name.value] = record
