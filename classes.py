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
    def __init__(self, name: Name, phone: Phone|None=None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.add_phone(phone)

    def __find_phone(self, phone: Phone) -> int|None:
        for i, item in  enumerate(self.phones):
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
    def add_record(self, record: Record):
        if record and type(record) == Record:
            self.data[record.name.value] = record
