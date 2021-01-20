from rest_framework.exceptions import ValidationError
from rest_framework import status


class UniqueError(ValidationError):
    default_code = 'unique'
    default_detail = 'field must be unique'


class ForeignKeyDoesNotExistError(ValidationError):
    default_code = 'does_not_exist'
    default_detail = 'Invalid pk, object does not exist.'


class InvalidType(ValidationError):
    ...
