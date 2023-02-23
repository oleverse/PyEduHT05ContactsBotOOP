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
    ab = AddressBook()

    for i in range(100):
        name = Name(f'Bill{i}')
        phone = Phone(str(i) * 8)
        birthday = Birthday("1983-12-23")
        rec = Record(name, phone, birthday)
        ab.add_record(rec)

    # assert isinstance(ab['Bill'], Record)
    # assert isinstance(ab['Bill'].name, Name)
    # assert isinstance(ab['Bill'].birthday, (Birthday, type(None)))
    # print(ab['Bill'].days_to_birthday())
    # assert isinstance(ab['Bill'].phones, list)
    # if ab['Bill'].phones:
    #     assert isinstance(ab['Bill'].phones[0], (Phone, type(None)))
    #     assert ab['Bill'].phones[0].value == '380957131551'

    for n, page in enumerate(ab.iterator(10)):
        print(f"Page-{n}:")
        print(page)

    print('All Ok)')