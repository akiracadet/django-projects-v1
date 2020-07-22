from django.forms import ModelForm
from todo.models import Todo

class CreateTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']
