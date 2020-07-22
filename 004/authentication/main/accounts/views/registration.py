from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from accounts.forms import *


class RegistrationView(View):
    template_name = 'accounts/registration.html'

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        context = {
            'form': RegistrationForm()
        }

        return render(request, self.template_name, context=context)


    def post(self, request):
        if request.user.is_authenticated:
            logout(request)

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('profile')

        context = {
            'form': form
        }

        return render(request, self.template_name, context=context)
