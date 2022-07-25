from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, DeleteView, DetailView, \
    UpdateView
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Tasks')
        return context


class DetailedTaskView(LoginRequiredMixin, SuccessMessageMixin, DetailView):

    model = Task
    template_name = 'tasks/task_view.html'
    context_object_name = 'task_view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task view')
        return context


class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Task
    form_class = TaskForm
    template_name = 'form.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully created.')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create a task')
        context['button_text'] = _('Create')
        return context


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'form.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully updated.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Change a task')
        context['button_text'] = _('Change')
        return context


class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully deleted.')

    def form_valid(self, form):
        if self.get_object().author == self.request.user:
            super().form_valid(form)
        else:
            messages.error(
                self.request,
                _('Task can be deleted only by author.'),
            )
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete a task')
        context['button_text'] = _('Yes, delete')
        return context