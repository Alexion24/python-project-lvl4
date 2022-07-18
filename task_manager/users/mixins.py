from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class UserMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.kwargs['pk'] == self.request.user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                _("You don't have permission to change another user.",)
            )
        else:
            self.success_url = 'login'
            messages.warning(
                self.request,
                _("You are not authorized. Please login."),
            )
        return redirect(self.success_url)
