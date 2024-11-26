from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


# Create your views here.
def home(request):
  return HttpResponse("<h1>Home</h1>")

def hello(request, username, id):
  return HttpResponse("<h1>Hello, %s (ID: %s)</h1>" % (username, id))

def about(request):
  return HttpResponse("<h1>About</h1>")

def projects(request):
  projects = list(Project.objects.values())
  return JsonResponse(projects, safe=False)

def project(request, id):
  # project = Project.objects.get(id=id)
  project = get_object_or_404(Project, id=id)
  return HttpResponse("<h1>Project: %s </h1>" % project.title)

def tasks(request):
  tasks = list(Task.objects.values())
  return JsonResponse(tasks, safe=False)

def task(request, id):
  # task = Task.objects.get(id=id)
  task = get_object_or_404(Task, id=id)
  return HttpResponse("<h1>Task: %s </h1>" % task.title)
