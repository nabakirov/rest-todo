from rest_framework.exceptions import ValidationError
from rest_framework import status


class UniqueError(ValidationError):
    default_code = 'unique'
    default_detail = 'field must be unique'


class ForeignKeyNotFoundError(ValidationError):
    default_code = 'not_found'
    default_detail = 'foreign key not found'
