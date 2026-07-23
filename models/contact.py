import importlib
import models.contact

importlib.reload(models.contact)

from models.contact import Contact
"""
contact.py

This module contains the Contact class which represents
a single contact in the Address Book System.
"""


class Contact:
    """
    Represents a single contact.

    Attributes:
        first_name (str): Contact's first name
        last_name (str): Contact's last name
        address (str): Street address
        city (str): City name
        state (str): State name
        zip_code (str): ZIP / Postal Code
        phone (str): Phone number
        email (str): Email address
    """

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
        """
        Constructor used to initialize a Contact object.
        """

        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.address = address.strip()
        self.city = city.strip()
        self.state = state.strip()
        self.zip_code = zip_code.strip()
        self.phone = phone.strip()
        self.email = email.strip()

    def __str__(self):
        """
        Returns a readable string representation of the Contact.
        """

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
        """
        Returns the official representation of the object.
        Useful while debugging.
        """

        return (
            f"Contact("
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}', "
            f"city='{self.city}', "
            f"phone='{self.phone}')"
        )

    def __eq__(self, other):
        """
        Compares two Contact objects.

        Two contacts are considered equal if
        both first name and last name are same
        (case-insensitive).
        """

        if not isinstance(other, Contact):
            return False

        return (
            self.first_name.lower() == other.first_name.lower()
            and self.last_name.lower() == other.last_name.lower()
        )     self.email = email