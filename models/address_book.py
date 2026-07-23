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
                    f"\nDuplicate Contact Found: "
                    f"{contact.first_name} {contact.last_name}\n"
                )
                return False

        self.contacts.append(contact)

        print(
            f"\nContact Added Successfully: "
            f"{contact.first_name} {contact.last_name}\n"
        )

        return True

    def edit_contact(
        self,
        first_name: str,
        last_name: str,
        address: str = None,
        city: str = None,
        state: str = None,
        zip_code: str = None,
        phone: str = None,
        email: str = None,
    ):
        """
        Edits an existing contact.
        """

        for contact in self.contacts:

            if (
                contact.first_name.lower() == first_name.lower()
                and contact.last_name.lower() == last_name.lower()
            ):

                if address is not None:
                    contact.address = address.strip()

                if city is not None:
                    contact.city = city.strip()

                if state is not None:
                    contact.state = state.strip()

                if zip_code is not None:
                    contact.zip_code = zip_code.strip()

                if phone is not None:
                    contact.phone = phone.strip()

                if email is not None:
                    contact.email = email.strip()

                print(
                    f"\nContact Updated Successfully: "
                    f"{contact.first_name} {contact.last_name}\n"
                )

                return True

        print(
            f"\nContact '{first_name} {last_name}' Not Found.\n"
        )

        return False

    def display_contacts(self):
        """
        Displays all contacts.
        """

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
        """
        Returns total number of contacts.
        """
        return len(self.contacts)