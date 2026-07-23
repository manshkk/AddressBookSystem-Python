"""
json_service.py

Handles JSON file operations
for the Address Book.
"""

import json
import os


class JSONService:

    FILE_PATH = "data/addressbook.json"

    @classmethod
    def save_contacts(cls, contacts):
        """
        Save contacts to a JSON file.
        """

        os.makedirs("data", exist_ok=True)

        contact_list = []

        for contact in contacts:

            contact_list.append({

                "first_name": contact.first_name,
                "last_name": contact.last_name,
                "address": contact.address,
                "city": contact.city,
                "state": contact.state,
                "zip_code": contact.zip_code,
                "phone": contact.phone,
                "email": contact.email

            })

        with open(
            cls.FILE_PATH,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                contact_list,
                file,
                indent=4
            )

        print("\nContacts saved to JSON successfully.\n")

    @classmethod
    def read_contacts(cls):
        """
        Read contacts from JSON file.
        """

        if not os.path.exists(cls.FILE_PATH):
            print("\nJSON file not found.\n")
            return

        with open(
            cls.FILE_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            contacts = json.load(file)

        print("\n========== CONTACTS FROM JSON ==========\n")

        for contact in contacts:
            print(contact)