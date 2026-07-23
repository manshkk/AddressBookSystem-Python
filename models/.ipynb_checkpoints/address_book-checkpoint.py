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

    # -------------------------------
    # Add Contact
    # -------------------------------

    def add_contact(self, contact: Contact):

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

    # -------------------------------
    # Edit Contact
    # -------------------------------

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

                print(
                    f"\nContact Updated Successfully: "
                    f"{contact.first_name} {contact.last_name}\n"
                )

                return True

        print("\nContact Not Found.\n")
        return False

    # -------------------------------
    # Delete Contact
    # -------------------------------

    def delete_contact(self, first_name, last_name):

        for contact in self.contacts:

            if (
                contact.first_name.lower() == first_name.lower()
                and contact.last_name.lower() == last_name.lower()
            ):

                self.contacts.remove(contact)

                print(
                    f"\nContact Deleted Successfully: "
                    f"{contact.first_name} {contact.last_name}\n"
                )

                return True

        print("\nContact Not Found.\n")
        return False

    # -------------------------------
    # Search by City
    # -------------------------------

    def search_by_city(self, city):

        found = False

        print(f"\nContacts in City : {city}")
        print("=" * 50)

        for contact in self.contacts:

            if contact.city.lower() == city.lower():

                print(contact)

                print("-" * 50)

                found = True

        if not found:
            print("No Contact Found.")
    def view_by_city(self):
    """
    Displays contacts grouped by city.
    """

    if not self.contacts:
        print("\nNo Contacts Available.\n")
        return

    city_dictionary = {}

    for contact in self.contacts:

        city = contact.city

        if city not in city_dictionary:
            city_dictionary[city] = []

        city_dictionary[city].append(contact)

    print("\n========== CONTACTS GROUPED BY CITY ==========\n")

    for city, contacts in city_dictionary.items():

        print(f"\nCity : {city}")
        print("-" * 50)

        for contact in contacts:
            print(contact)
            print("-" * 50)

    def count_by_city(self):
    """
    Counts contacts in each city.
    """

    if not self.contacts:
        print("\nNo Contacts Available.\n")
        return

    city_count = {}

    for contact in self.contacts:

        city = contact.city

        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1

    print("\n========== CONTACT COUNT BY CITY ==========\n")

    for city, count in city_count.items():
        print(f"{city:<20} : {count}")

    # -------------------------------
    # Search by State
    # -------------------------------

    def search_by_state(self, state):

        found = False

        print(f"\nContacts in State : {state}")
        print("=" * 50)

        for contact in self.contacts:

            if contact.state.lower() == state.lower():

                print(contact)

                print("-" * 50)

                found = True

        if not found:
            print("No Contact Found.")

    def view_by_state(self):
    """
    Displays contacts grouped by state.
    """

    if not self.contacts:
        print("\nNo Contacts Available.\n")
        return

    state_dictionary = {}

    for contact in self.contacts:

        state = contact.state

        if state not in state_dictionary:
            state_dictionary[state] = []

        state_dictionary[state].append(contact)

    print("\n========== CONTACTS GROUPED BY STATE ==========\n")

    for state, contacts in state_dictionary.items():

        print(f"\nState : {state}")
        print("-" * 50)

        for contact in contacts:
            print(contact)
            print("-" * 50)

    def count_by_state(self):
    """
    Counts contacts in each state.
    """

    if not self.contacts:
        print("\nNo Contacts Available.\n")
        return

    state_count = {}

    for contact in self.contacts:

        state = contact.state

        if state in state_count:
            state_count[state] += 1
        else:
            state_count[state] = 1

    print("\n========== CONTACT COUNT BY STATE ==========\n")

    for state, count in state_count.items():
        print(f"{state:<20} : {count}")

    def sort_by_name(self):
    """
    Displays contacts sorted alphabetically by first name,
    then last name.
    """

    if not self.contacts:
        print("\nNo Contacts Available.\n")
        return

    sorted_contacts = sorted(
        self.contacts,
        key=lambda contact: (
            contact.first_name.lower(),
            contact.last_name.lower()
        )
    )

    print("\n========== CONTACTS SORTED BY NAME ==========\n")

    for index, contact in enumerate(sorted_contacts, start=1):

        print(f"\nContact {index}")

        print(contact)

        print("-" * 50)

    # -------------------------------
    # Display Contacts
    # -------------------------------

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

    # -------------------------------
    # Total Contacts
    # -------------------------------

    def total_contacts(self):

        return len(self.contacts)