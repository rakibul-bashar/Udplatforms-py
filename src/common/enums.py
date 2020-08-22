from django.utils.translation import gettext as _
from django.db import models


class UserTypes(models.TextChoices):
    PARENT = 'PARENT', _('Parent')
    CHILD = 'CHILD', _('Child')
