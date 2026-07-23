"""
csv_service.py

Handles CSV file operations
for the Address Book.
"""

import csv
import os


class CSVService:

    FILE_PATH = "data/addressbook.csv"

    @classmethod
    def save_contacts(cls, contacts):
        """
        Save contacts into CSV file.
        """

        os.makedirs("data", exist_ok=True)

        with open(
            cls.FILE_PATH,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            # Header Row
            writer.writerow([
                "First Name",
                "Last Name",
                "Address",
                "City",
                "State",
                "Zip Code",
                "Phone",
                "Email"
            ])

            # Data Rows
            for contact in contacts:

                writer.writerow([
                    contact.first_name,
                    contact.last_name,
                    contact.address,
                    contact.city,
                    contact.state,
                    contact.zip_code,
                    contact.phone,
                    contact.email
                ])

        print("\nContacts saved to CSV successfully.\n")

    @classmethod
    def read_contacts(cls):
        """
        Read contacts from CSV file.
        """

        if not os.path.exists(cls.FILE_PATH):
            print("\nCSV file not found.\n")
            return

        print("\n========== CONTACTS FROM CSV ==========\n")

        with open(
            cls.FILE_PATH,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            next(reader)  # Skip header

            for row in reader:
                print(row)