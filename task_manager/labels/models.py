from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(_('name'), max_length=50, null=False)
    created_at = models.DateTimeField(_('creation date'), auto_now_add=True)

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')
        ordering = ['id']

    def __str__(self):
        return self.name
