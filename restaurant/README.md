
The main purpose of this assignment is to design the web page of WCAG 1.0. The WCAG documents explain how to make web content more accessible to people with disabilities.  The WCAG is the part of the web accessibility published by the Web Accessibility Initiative. The objective of that organization was that the page will be maxim accessible possible for all the people. In WCAG documents, we can find the different points that the page or the application have to accomplish. WCAG 1.0 has the 14 guidelines in which each of them describes a general principle of accessible design.

The assignment is divided into two parts:

First of all, in this assignment, we have make the classes in Django program which will be connected with the Django administration. The classes came from our UML design and in the Django administration, we can find all the classes and attributes of each class. Furthermore, we have to give access to the user that we can add, modify and delete the things in the Django administration. In this part, we also have to do the login part in which after the login the page will show you the built-in message that we have given to the page.

In the second part, we have deployments. In the first one, we have to deploy the Django application in Heroku. In the second one, we have to deploy the Django application as a docker using the docker container and finally, we have to explain how to deploy the application to the multiple servers.

### First Part of this assignment

The first and second point of our activity is connected with each other. To make the first part, we have transformed our UML design into classes of the Django application. In each class, we can find different attributes in which some are the string, integer or date attributes. In some classes, we can find some foreign key attributes that mean they are related to one too many relationships of the data model of the database and we have also many to many relationship database models. In our case, we have 8 classes which are related to each other with different database relationship. As an example, we can look at the class nextly:
class Client(models.Model):
    nif = models.TextField()
    Fname = models.CharField(max_length=120)

The classes are located in the models.py which is located in clients fil. The registration of the attributes is located in the same folder and in the admin file.

In the second point, we have given access to the user to add, modify and delete things of the attributes. That point, we have done using the command python manage.py migrate in which creates the database. If we have done migrations correctly then we can make the addition, modification, and deletion of the things.

For the third point of the activity, we have made the modification in settings.py and urls.py. For the built-in message, we have created the python file “views.py” in which we have the message that will print after the login. For the login, we have created the templates folder and create the login.html file in which we have the login structure.

###Things added in settungs.py
'DIRS': ['templates']
LOGIN_REDIRECT_URL = '/built/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

###Things added in urls.py

path('login/',views.login),
path('built/', root_views.built),
from django.contrib.auth import views
from . import views as root_views

### Fourth point of this assignment
### 12th guidelines

As we said before, we have the login and views python files located in different folders where we found the structure of the session and the view of the built-in message.

1- base code:
We comply with this first rule as there is only one base code, it is managed from a version system (Github), there is a ratio of 1 to 1 between the base code and the application. All versions of each deployment share the same code.

2- Dependencies
We only use bookstores that are part of the code and standard libraries of Django to not depend on any system tool, because all systems do not have the same tools.

3- config
We do not have configurations that handle the database externally, it does not include internal configurations. To verify that we comply with this rule, we would simply put the code in open source and we would not compromise the credentials.

4- backing services
For now, our project is a local service because at the moment we do not have any external service, therefore we comply with this norm

5-Build, release, run
As it is still under development, we have only done the first stage, the one to build our project

6-Processes
The simplest case that must be met is ours, run the program on a development laptop and all work correctly. Any persistent value or any data that lasts in times we store it in a banking service (local database).

7-Port binding
We do not rely on any web server to execute our project since we execute it from our localhost development environment.
8-Concurrency
Our project at the moment is not concurrently because it is done with different classes within our project

9-Disposability
If we unexpectedly cut off the connection, we will all leave an error message with the server and the connection will be cut.

10- Dev/prod parity:
We are continually developing code versions of our versions to have a similar code all the time.

We do not have a history since we print all the events for the terminal because we do not save the directions or the transmissions of exit.

12- Admin processes:
There are processes that we only perform once or twice during the usual tasks of the project how to process requests, web, execute migrations of databases, execute a console ...
All of these processes are always running the same with the same base code and the same configuration. And the same isolation technique is used in all processes.  


### Second Part of this assignment

In the second part of this assignment, we have different deployments of the Django application. In the first case, we have the Django application deployed into Heroku. To make this deployment, we have done some modification in the settings python file and we could easily deploy it on Heroku simply adding your Heroku app branch to the git already existing on this project. we have done the deployment with the following steps:

### Heroku login

Add a Procfile in the project root directory to define process types and explicitly declare what command should be executed to start your app.
pip install gunicorn dj-database-url whitenoise psycopg2
pip freeze > requirements.txt

# addicition in the settings.py:

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
django_heroku.settings(locals())
ALLOWED_HOSTS = ['myfirstexperience.herokuapp.com']

# adding our Heroku app branch to the git

git init
git status
git add -A
git commit -m "update settings_require"
git push heroku master

##And you will have it deployed on Heroku

In the second case, we have to deploy the Django project into docker. Doing the deployment, we will able to connect the application with the address. In our case, we have done the deployment using the docker container. To make it possible we have used the following commands:

docker-compose build
docker-compose up
made the docker and docker-compose.yml files
pip freeze > requirements.txt

### THIRD POINT OF DEPLOYMENT OF THIS PART

In this point, we have to explain how the deployment works for the multiple servers. We have four types of runners for the Django application as we can look nextly:

Running on a single server: mostly the sites runs on the single server because as the traffic increases in the application, we can quickly run into resource contention between the different pieces of the software. In this runner, the database server and web server runs on the same servers so, they often end up fighting over the same resources like CPU, RAM, etc and they don't prefer to monopolize the resources.

Separation of the database server: for the separation of the database server is extremely easy, we will simply need to change the database_host settings to the IP or DNS name of our server. It is good to use the IP because as relying on DNS for the connection between your Web server and the database server isn’t recommended. Here, the architecture that they are going to use called n-tier architecture. In this architecture, the different tiers of the web stack get separated onto different physical machines. If we want to grow the database server, it is a good idea to start thinking about connection pooling and database replication.

Separate media server: we have the big problem left over the single server setup because of the serving of media from the same box that handles the dynamic content. The two activities are working under different circumstances but smashing each other in the same box.

The media server should be a stripped-down web server optimized for static media delivery. In this case, the preferable option for this server is Nginx but, we can also use apache for the heavily stripped. It is important to use a separate media server for heavy sites in static content. If our Django application has the uploads files so, Django needs to be able to write uploaded media to the media server. Moreover, if the media needs another server, so we have to arrange some way that writes to happen across the network.
