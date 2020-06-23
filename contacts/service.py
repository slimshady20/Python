from contacts.model import Model


class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload):
        print('입력된 이름 ' + payload)
        for i in self._contacts:
            if payload == i.name:
                return i

    def get_contacts(self):
        return self._contacts

    def del_contact(self, payload):  # none
        pass
