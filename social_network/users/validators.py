import re

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError


PHONE_REGEXP = '^[+]?[\d]{8,15}$'


class PhoneRegexValidator(RegexValidator):

    def __call__(self, value):
        if not isinstance(value, str):
            raise ValidationError('Wrong type of phone number.')
        value = self.clean_phone(value)
        super().__call__(value)

    @classmethod
    def clean_phone(cls, value):
        return re.sub('[^+\d]', '', value)


phone_validator = PhoneRegexValidator(PHONE_REGEXP,
                                      message=_('Invalid phone number'))
