import csv
from pathlib import Path


class CSVService:

    FILE_PATH = Path("data/addressbook.csv")

    def __init__(self):
        self.FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    def save_contacts(self, contacts):

        try:

            with open(self.FILE_PATH, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow(
                    [
                        "First Name",
                        "Last Name",
                        "Address",
                        "City",
                        "State",
                        "Zip Code",
                        "Phone",
                        "Email",
                    ]
                )

                for contact in contacts:

                    writer.writerow(
                        [
                            contact.first_name,
                            contact.last_name,
                            contact.address,
                            contact.city,
                            contact.state,
                            contact.zip_code,
                            contact.phone,
                            contact.email,
                        ]
                    )

            return True

        except PermissionError:
            raise PermissionError(
                "Permission denied while writing CSV file."
            )

        except csv.Error as error:
            raise csv.Error(
                f"CSV write error: {error}"
            )

        except OSError as error:
            raise OSError(
                f"Unable to save CSV file: {error}"
            )

    def read_contacts(self):

        try:

            if not self.FILE_PATH.exists():
                raise FileNotFoundError(
                    "CSV file does not exist."
                )

            contacts = []

            with open(self.FILE_PATH, "r", newline="") as file:

                reader = csv.reader(file)

                next(reader, None)

                for row in reader:
                    contacts.append(row)

            return contacts

        except FileNotFoundError:
            raise

        except PermissionError:
            raise PermissionError(
                "Permission denied while reading CSV file."
            )

        except csv.Error as error:
            raise csv.Error(
                f"CSV read error: {error}"
            )

        except OSError as error:
            raise OSError(
                f"Unable to read CSV file: {error}"
            )