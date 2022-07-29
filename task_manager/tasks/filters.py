from django_filters import FilterSet
from django_filters.filters import ChoiceFilter, BooleanFilter
from django.forms import CheckboxInput
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.translation import gettext as _
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class TasksFilter(FilterSet):

    all_statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = ChoiceFilter(label=_('Status'), choices=all_statuses)
    all_labels = Label.objects.values_list('id', 'name', named=True).all()
    labels = ChoiceFilter(label=_('Label'), choices=all_labels)
    all_executors = User.objects.values_list(
        'id',
        Concat('first_name', Value(" "), 'last_name'),
        named=True,
    ).all()
    executor = ChoiceFilter(label=_('Executor'), choices=all_executors)
    self_task = BooleanFilter(
        label=_('Only my tasks'),
        widget=CheckboxInput(),
        method="filter_self",
        field_name="self_task",
    )

    def filter_self(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
