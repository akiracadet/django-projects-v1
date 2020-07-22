from django.urls import path
from todo.views import TodoView, TodoDeleteView

urlpatterns = [
    path('', TodoView.as_view(), name='todo-index'),
    path('index/', TodoView.as_view(), name='todo-index'),

    path('delete/<pk>/', TodoDeleteView.as_view(), name='todo-delete'),
]
