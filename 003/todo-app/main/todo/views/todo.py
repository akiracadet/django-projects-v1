from django.shortcuts import redirect, render
from django.views import View
from todo.forms import CreateTodoForm
from todo.models import Todo


class TodoView(View):
    template_name = 'todo/index.html'

    def get(self, request):
        form = CreateTodoForm()
        todos = Todo.objects.all()

        return render(request, self.template_name, context={
            'todos': todos,
            'form': form,
        })


    def post(self, request):
        todos = Todo.objects.all()
        form = CreateTodoForm(request.POST)

        if form.is_valid():
            if request.POST.get('add_todo') == 'add_todo':
                form.save()


            return redirect('todo-index')

        return render(request, self.template_name, context={
            'todos': todos,
            'form': form,
        })
