"""
address_book.py
---------------

Defines the AddressBook class that stores multiple contacts.
"""

from models.contact import Contact


class AddressBook:
    """
    Represents a single Address Book.

    An AddressBook stores multiple Contact objects.
    """

    def __init__(self, name: str):
        self.name = name.strip()
        self.contacts = []

    def add_contact(self, contact: Contact):
        """
        Adds a Contact object to the address book.
        """
        self.contacts.append(contact)

    def display_contacts(self):
        """
        Displays all contacts stored in the address book.
        """
        if not self.contacts:
            print("\nNo contacts found.\n")
            return

        print(f"\nAddress Book : {self.name}")
        print("-" * 50)

        for index, contact in enumerate(self.contacts, start=1):
            print(f"\nContact {index}")
            print(contact)
            print("-" * 50)

    def total_contacts(self):
        """
        Returns the total number of contacts.
        """
        return len(self.contacts)