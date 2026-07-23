import re

from exceptions.custom_exceptions import (
    InvalidPhoneNumberException,
    InvalidEmailException,
    InvalidZipCodeException,
)


class Contact:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        address: str,
        city: str,
        state: str,
        zip_code: str,
        phone: str,
        email: str,
    ):
        first_name = first_name.strip()
        last_name = last_name.strip()
        address = address.strip()
        city = city.strip()
        state = state.strip()
        zip_code = zip_code.strip()
        phone = phone.strip()
        email = email.strip()

        if not phone.isdigit() or len(phone) != 10:
            raise InvalidPhoneNumberException(
                "Phone number must contain exactly 10 digits."
            )

        if not zip_code.isdigit() or len(zip_code) != 6:
            raise InvalidZipCodeException(
                "Zip code must contain exactly 6 digits."
            )

        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.fullmatch(email_pattern, email):
            raise InvalidEmailException("Invalid email address.")

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):

        return (
            f"\n"
            f"First Name : {self.first_name}\n"
            f"Last Name  : {self.last_name}\n"
            f"Address    : {self.address}\n"
            f"City       : {self.city}\n"
            f"State      : {self.state}\n"
            f"Zip Code   : {self.zip_code}\n"
            f"Phone      : {self.phone}\n"
            f"Email      : {self.email}"
        )

    def __repr__(self):

        return (
            f"Contact("
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}', "
            f"city='{self.city}', "
            f"phone='{self.phone}')"
        )

    def __eq__(self, other):

        if not isinstance(other, Contact):
            return False

        return (
            self.first_name.lower() == other.first_name.lower()
            and self.last_name.lower() == other.last_name.lower()
        )