class AddressBookException(Exception):
    pass


class DuplicateContactException(AddressBookException):
    pass


class ContactNotFoundException(AddressBookException):
    pass


class InvalidPhoneNumberException(AddressBookException):
    pass


class InvalidEmailException(AddressBookException):
    pass


class InvalidZipCodeException(AddressBookException):
    pass