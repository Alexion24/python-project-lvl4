from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label


class LabelsListView(LoginRequiredMixin, ListView):

    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Labels')
        return context


class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Label
    form_class = LabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully created.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create a label')
        context['button_text'] = _('Create')
        return context


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Label
    form_class = LabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully updated.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Change a label')
        context['button_text'] = _('Change')
        return context


class DeleteLabelView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully deleted.')

    def form_valid(self, form):
        if self.get_object().tasks.all():
            messages.error(
                self.request,
                _('Cannot delete label because it is in use')
            )
        else:
            super().form_valid(form)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete label')
        context['button_text'] = _('Yes, delete')
        return context
