from pathlib import Path


class FileService:

    FILE_PATH = Path("data/addressbook.txt")

    def __init__(self):
        self.FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    def save_contacts(self, contacts):

        try:

            with open(self.FILE_PATH, "w") as file:

                for contact in contacts:

                    file.write(str(contact))
                    file.write("\n")
                    file.write("-" * 50)
                    file.write("\n")

            return True

        except PermissionError:
            raise PermissionError(
                "Permission denied while writing to the file."
            )

        except OSError as error:
            raise OSError(
                f"Unable to save contacts: {error}"
            )

    def read_contacts(self):

        try:

            if not self.FILE_PATH.exists():
                raise FileNotFoundError(
                    "Address book file does not exist."
                )

            with open(self.FILE_PATH, "r") as file:
                return file.read()

        except FileNotFoundError:
            raise

        except PermissionError:
            raise PermissionError(
                "Permission denied while reading the file."
            )

        except OSError as error:
            raise OSError(
                f"Unable to read contacts: {error}"
            )