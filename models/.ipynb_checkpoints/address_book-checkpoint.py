"""
address_book.py
---------------

Defines the AddressBook class.
"""

from models.contact import Contact


class AddressBook:
    """
    Represents one Address Book.
    """

    def __init__(self, name: str):
        self.name = name.strip()
        self.contacts = []

    def add_contact(self, contact: Contact):
        """
        Adds a contact after checking duplicates.
        """

        for existing_contact in self.contacts:

            if existing_contact == contact:
                print(
                    f"\nDuplicate Contact Found:"
                    f" {contact.first_name} {contact.last_name}\n"
                )
                return False

        self.contacts.append(contact)

        print(
            f"\nContact Added Successfully:"
            f" {contact.first_name} {contact.last_name}\n"
        )

        return True

    def display_contacts(self):

        if not self.contacts:
            print("\nNo Contacts Available\n")
            return

        print(f"\nAddress Book : {self.name}")
        print("=" * 50)

        for index, contact in enumerate(self.contacts, start=1):

            print(f"\nContact {index}")

            print(contact)

            print("-" * 50)

    def total_contacts(self):
        return len(self.contacts)