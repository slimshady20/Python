from contacts import service
from contacts.model import Model
from contacts.service import Service


class Controller:
    def __init__(self):
        self._service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name
        model.phone = phone
        model.email = email
        model.addr = addr
        self._service.add_contact(model)

    def search(self, payload):
        return self._service.get_contact(payload)

    def list(self):
        return self._service.get_contacts()

    def remove(self):
        pass
