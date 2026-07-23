"""
file_service.py
---------------

Handles reading and writing contacts
to a text file.
"""

import os


class FileService:

    FILE_PATH = "data/addressbook.txt"

    @classmethod
    def save_contacts(cls, contacts):
        """
        Saves contacts to a text file.
        """

        os.makedirs("data", exist_ok=True)

        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:

            for contact in contacts:

                file.write(
                    f"{contact.first_name},"
                    f"{contact.last_name},"
                    f"{contact.address},"
                    f"{contact.city},"
                    f"{contact.state},"
                    f"{contact.zip_code},"
                    f"{contact.phone},"
                    f"{contact.email}\n"
                )

        print("\nContacts saved successfully.\n")

    @classmethod
    def read_contacts(cls):

        if not os.path.exists(cls.FILE_PATH):
            print("\nNo saved file found.\n")
            return

        print("\n========== SAVED CONTACTS ==========\n")

        with open(cls.FILE_PATH, "r", encoding="utf-8") as file:

            for line in file:
                print(line.strip())