
pip install virtualenv

.venv\Scripts\activate

pip install django


django-admin --version

django-admin startproject mysite .


python manage.py runserver
<!-- python manage.py runserver 3000 -->

python manage.py --help

python manage.py startapp myapp

python manage.py makemigrations
<!-- python manage.py makemigrations myapp -->

python manage.py migrate
<!-- python manage.py migrate myapp -->

python manage.py shell

from myapp.models import Project, Task

p = Project(title="mobile app", description="mobile application project")
p
p.save()

p = Project(title="web app", description="web application project")
p
p.save()

Project.objects.all()
Project.objects.get(id=1)
Project.objects.get(id=2)
Project.objects.get(title="mobile app")

exit()

python manage.py shell

from myapp.models import Project, Task

p = Project.objects.get(id=1)
p
p.task_set.all()
p.task_set.create(title="mobile app task", description="mobile application task")
p.task_set.create(title="mobile app second task", description="mobile application second task")
p.task_set.get(id=1)

<!-- Project.objects.filter(title__startswith="web") -->
p = Project.objects
p.filter(title__startswith="web")

python manage.py runserver

python manage.py createsuperuser
