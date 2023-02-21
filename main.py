from classes import *


# if __name__ == "__main__":
#     ab = AddressBook()

#     petro = Record("Petro")
#     petro.add_phone("0950959595")

#     ab.add_record(petro)
#     print(ab["Petro"].phones[0].value)

#     petro.edit_phone(current_value="0950959595", new_value="0000000000")
#     print(ab["Petro"].phones[0].value)

#     print(len(ab["Petro"].phones))

#     petro.del_phone("0000000000")

#     print(len(ab["Petro"].phones))

if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')