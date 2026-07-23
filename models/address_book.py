from models.contact import Contact
from exceptions.custom_exceptions import (
    DuplicateContactException,
    ContactNotFoundException,
)


class AddressBook:

    def __init__(self, name: str):
        self.name = name.strip()
        self.contacts = []

    def add_contact(self, contact: Contact):

        for existing_contact in self.contacts:

            if existing_contact == contact:
                raise DuplicateContactException(
                    f"Contact '{contact.first_name} {contact.last_name}' already exists."
                )

        self.contacts.append(contact)

        return True

    def edit_contact(
        self,
        first_name,
        last_name,
        address=None,
        city=None,
        state=None,
        zip_code=None,
        phone=None,
        email=None,
    ):

        for contact in self.contacts:

            if (
                contact.first_name.lower() == first_name.lower()
                and contact.last_name.lower() == last_name.lower()
            ):

                if address is not None:
                    contact.address = address

                if city is not None:
                    contact.city = city

                if state is not None:
                    contact.state = state

                if zip_code is not None:
                    contact.zip_code = zip_code

                if phone is not None:
                    contact.phone = phone

                if email is not None:
                    contact.email = email

                return True

        raise ContactNotFoundException(
            f"Contact '{first_name} {last_name}' not found."
        )

    def delete_contact(self, first_name, last_name):

        for contact in self.contacts:

            if (
                contact.first_name.lower() == first_name.lower()
                and contact.last_name.lower() == last_name.lower()
            ):

                self.contacts.remove(contact)

                return True

        raise ContactNotFoundException(
            f"Contact '{first_name} {last_name}' not found."
        )

    def search_by_city(self, city):

        contacts = [
            contact
            for contact in self.contacts
            if contact.city.lower() == city.lower()
        ]

        return contacts

    def search_by_state(self, state):

        contacts = [
            contact
            for contact in self.contacts
            if contact.state.lower() == state.lower()
        ]

        return contacts

    def view_by_city(self):

        city_dictionary = {}

        for contact in self.contacts:
            city_dictionary.setdefault(contact.city, []).append(contact)

        return city_dictionary

    def view_by_state(self):

        state_dictionary = {}

        for contact in self.contacts:
            state_dictionary.setdefault(contact.state, []).append(contact)

        return state_dictionary

    def count_by_city(self):

        city_count = {}

        for contact in self.contacts:
            city_count[contact.city] = city_count.get(contact.city, 0) + 1

        return city_count

    def count_by_state(self):

        state_count = {}

        for contact in self.contacts:
            state_count[contact.state] = state_count.get(contact.state, 0) + 1

        return state_count

    def sort_by_name(self):

        return sorted(
            self.contacts,
            key=lambda contact: (
                contact.first_name.lower(),
                contact.last_name.lower(),
            ),
        )

    def sort_by_city(self):

        return sorted(
            self.contacts,
            key=lambda contact: (
                contact.city.lower(),
                contact.first_name.lower(),
                contact.last_name.lower(),
            ),
        )

    def sort_by_state(self):

        return sorted(
            self.contacts,
            key=lambda contact: (
                contact.state.lower(),
                contact.first_name.lower(),
                contact.last_name.lower(),
            ),
        )

    def sort_by_zip(self):

        return sorted(
            self.contacts,
            key=lambda contact: contact.zip_code,
        )

    def display_contacts(self):

        return self.contacts

    def total_contacts(self):

        return len(self.contacts)