import json
from pathlib import Path


class JSONService:

    FILE_PATH = Path("data/addressbook.json")

    def __init__(self):
        self.FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    def save_contacts(self, contacts):

        try:

            data = []

            for contact in contacts:

                data.append(
                    {
                        "first_name": contact.first_name,
                        "last_name": contact.last_name,
                        "address": contact.address,
                        "city": contact.city,
                        "state": contact.state,
                        "zip_code": contact.zip_code,
                        "phone": contact.phone,
                        "email": contact.email,
                    }
                )

            with open(self.FILE_PATH, "w") as file:
                json.dump(data, file, indent=4)

            return True

        except PermissionError:
            raise PermissionError(
                "Permission denied while writing JSON file."
            )

        except TypeError as error:
            raise TypeError(
                f"JSON serialization error: {error}"
            )

        except OSError as error:
            raise OSError(
                f"Unable to save JSON file: {error}"
            )

    def read_contacts(self):

        try:

            if not self.FILE_PATH.exists():
                raise FileNotFoundError(
                    "JSON file does not exist."
                )

            with open(self.FILE_PATH, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            raise

        except json.JSONDecodeError as error:
            raise json.JSONDecodeError(
                error.msg,
                error.doc,
                error.pos,
            )

        except PermissionError:
            raise PermissionError(
                "Permission denied while reading JSON file."
            )

        except OSError as error:
            raise OSError(
                f"Unable to read JSON file: {error}"
            )