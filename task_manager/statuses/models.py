from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):

    name = models.CharField(_('name'), max_length=30)
    created_at = models.DateTimeField(_('creation date'), auto_now_add=True)

    class Meta:

        verbose_name = _('status')
        verbose_name_plural = _('statuses')
        ordering = ['id']

    def __str__(self):
        return self.name
