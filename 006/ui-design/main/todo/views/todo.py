from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from todo.forms import CreateTodoForm
from todo.models import Todo


class TodoView(LoginRequiredMixin, View):
    template_name = 'todo/index.html'
    login_url = 'login'

    def get(self, request):
        print(request.user)
        todos = Todo.objects.filter(user=request.user)
        form = CreateTodoForm()

        return render(request, self.template_name, context={
            'todos': todos,
            'form': form,
        })


    def post(self, request):
        print(request.user)

        todos = Todo.objects.filter(user=request.user)
        form = CreateTodoForm(request.POST)

        if form.is_valid():
            if request.POST.get('add_todo') == 'add_todo':
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()

            return redirect('todo-index')

        return render(request, self.template_name, context={
            'todos': todos,
            'form': form,
        })
