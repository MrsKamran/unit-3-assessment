from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
from django.views.generic.edit import  DeleteView
from django.db.models import Sum

# def deleteTask(request):
class TaskDelete(DeleteView):
    model = Task
    success_url = "/"

def createTask(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.save()
    return redirect('main:index')
  

def index(request):
  task_list = Task.objects.all()
  total_time = Task.objects.aggregate(Sum('time'))
  task_form = TaskForm()
  context = {'task_list': task_list,'task_form':task_form, 'total_time':total_time}
  return render(request, 'main/index.html', context)

