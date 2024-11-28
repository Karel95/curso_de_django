from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/<str:username>/<int:id>', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    path('project/<int:id>', views.project, name='project'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:id>', views.task, name='task'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_task/', views.create_task, name='create_task'),
]
