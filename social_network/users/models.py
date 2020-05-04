from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """
    Custom User model
    """
    phone = models.CharField(_('Phone number'),
                             max_length=100,
                             null=True,
                             blank=True)
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50,
                                  blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'

    def __str__(self):
        return self.email
