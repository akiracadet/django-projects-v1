from django.contrib.auth.views import LogoutView as _LogoutView


class LogoutView(_LogoutView):
    next_page = 'login'
