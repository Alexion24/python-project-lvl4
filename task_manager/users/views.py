from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from task_manager.users.models import User
from task_manager.users.forms import CreateUserForm
from task_manager.users.mixins import UserMixin


class UserListView(ListView):

    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Users')
        return context


class CreateUserView(SuccessMessageMixin, CreateView):

    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = _('User successfully registered.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Registration')
        context['button_text'] = _('Register')
        return context


class UpdateUserView(SuccessMessageMixin, UserMixin, UpdateView):

    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('users:users')
    success_message = _('User successfully changed.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Change a user')
        context['button_text'] = _('Change')
        return context


class DeleteUserView(SuccessMessageMixin, UserMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users:users')
    success_message = _('User successfully deleted.')

    def form_valid(self, form):
        if self.get_object().author.all() or self.get_object().executor.all():
            messages.error(
                self.request,
                _('Cannot delete user because it is in use')
            )
        else:
            super().form_valid(form)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete a user')
        context['button_text'] = _('Yes, delete')
        return context
