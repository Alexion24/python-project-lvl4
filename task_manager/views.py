from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class IndexView(TemplateView):

    template_name = 'index.html'


class LoginUserView(SuccessMessageMixin, LoginView):

    template_name = 'form.html'
    success_message = _('You successfully logged in')
    next_page = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Login')
        context['button_text'] = _('Login')
        return context


class LogoutUserView(SuccessMessageMixin, LogoutView):

    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(
            request,
            messages.INFO,
            _('You logged out successfully')
        )
        return super().dispatch(request, *args, **kwargs)
