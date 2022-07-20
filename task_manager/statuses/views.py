from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm


class StatusesListView(LoginRequiredMixin, ListView):

    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Statuses')
        return context


class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully created.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create a status')
        context['button_text'] = _('Create')
        return context


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully changed.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Change a status')
        context['button_text'] = _('Change')
        return context


class DeleteStatusView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully deleted.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete a status')
        context['button_text'] = _('Yes, delete')
        return context
