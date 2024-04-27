from django.core.validators import RegexValidator


def validate_patent(value):
    pattern = r'^[A-Z]{2} \d{3} [A-Z]{2}$'
    validate = RegexValidator(regex=pattern, message='El formato de la patente debe ser AZ 123 BC')
    validate(value)