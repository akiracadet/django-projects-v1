from django.shortcuts import redirect, render
from django.views import View
from todo.models import Todo


class TodoDeleteView(View):
    template_name = 'todo/delete.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=None)


    def post(self, request, *args, **kwargs):
        if 'yes_delete_todo' in request.POST:
            if 'pk' in kwargs:
                Todo.objects.get(pk=kwargs['pk']).delete()

        return redirect('todo-index')
