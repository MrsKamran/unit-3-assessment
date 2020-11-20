
from django.urls import path
from .import views
from main.views import TaskDelete

app_name = 'main'
urlpatterns = [

    path('', views.index, name='index'),
    path('create/', views.createTask, name='create'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='delete'),
]

