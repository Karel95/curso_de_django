from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hello/<str:username>/<int:id>', views.hello),
    path('about/', views.about),
    path('projects/', views.projects),
    path('project/<int:id>', views.project),
    path('tasks/', views.tasks),
    path('task/<int:id>', views.task),
    path('create_project/', views.create_project),
    path('create_task/', views.create_task),
]
