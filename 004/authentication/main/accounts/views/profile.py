from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as UserModel
from django.shortcuts import render
from django.views import View


class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    login_url = 'login'

    def get(self, request):
        user = UserModel.objects.get(pk=request.user.pk)
        tmp = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
        user = tmp

        context = {'user': user}

        return render(request, self.template_name, context=context)
