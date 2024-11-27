from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


# Create your views here.
def home(request):
  h1 = 'My Django App'
  return render(request, 'index.html', {
    'title': h1,
  })

def about(request):
  return render(request, 'about.html')

def hello(request, username, id):
  return HttpResponse("<h1>Hello, %s (ID: %s)</h1>" % (username, id))

def projects(request):
  # projects = list(Project.objects.values())
  # return JsonResponse(projects, safe=False)
  projects = Project.objects.all()
  return render(request, 'projects.html', {
    'projects': projects
  })

def project(request, id):
  # project = Project.objects.get(id=id)
  project = get_object_or_404(Project, id=id)
  return HttpResponse("<h1>Project: %s </h1>" % project.title)

def tasks(request):
  # tasks = list(Task.objects.values())
  # return JsonResponse(tasks, safe=False)
  return render(request, 'tasks.html')

def task(request, id):
  # task = Task.objects.get(id=id)
  task = get_object_or_404(Task, id=id)
  return HttpResponse("<h1>Task: %s </h1>" % task.title)
