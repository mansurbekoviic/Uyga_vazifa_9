from django.core.exceptions import ValidationError

def validate_positive(value):
    if value <= 0:
        raise ValidationError('Qiymat musbat bo‘lishi kerak!')
