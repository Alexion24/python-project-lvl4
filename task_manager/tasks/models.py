from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        related_name='status',
        verbose_name=_('status'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name='author',
        verbose_name=_('author')
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name='executor',
        verbose_name=_('Executor'),
    )
    created_at = models.DateTimeField(_('created date'), auto_now_add=True)

    class Meta:

        verbose_name = _('task')
        verbose_name_plural = _('tasks')
        ordering = ['id']

    def __str__(self):
        return self.name
