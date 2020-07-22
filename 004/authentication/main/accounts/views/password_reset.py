from django.contrib.auth.views import PasswordResetView as _PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView as _PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView as _PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView as _PasswordResetCompleteView


class PasswordResetView(_PasswordResetView):
    template_name = 'accounts/password_reset.html'


class PasswordResetDoneView(_PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(_PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'


class PasswordResetCompleteView(_PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
