from django.urls import path
from home.views.home import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('index', HomeView.as_view(), name='home'),
]
