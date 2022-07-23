## Lab1 Objectives:

To setup the development environment; start project based on django
To create remote and local repository
To perform basic operations like git clone, commit, push & pull

---

## Introduction:

The very first lab of electronic commerce was focused of setup and integration of development kits. This session was basic and fundamental to start a project. We mainly focused to install IDE, Framework Integration, Git and etc.

---

## Procedures(Steps/Code):

1.  django-admin startproject ecommerce_lab1
    or
    python -m django-admin startproject ecommerce_lab1

2.  cd ecommerce_lab1

3.  Initialize database:
    python manage.py migrate

4.  CREATE Super User
    python manage.py createsuperuser

5.  Run the project
    python manage.py runserver

6.  Ips:
    127.0.0.1:8000
    127.0.0.1:8000/admin

7.  Entry point command : manage.py
    wsgi.py - helps to turn on your laptop as a server and helps to run your code [guicorn, ]
    urls.py - to congtain urls
    asgi.py - similar to wsgi.py
    setting.py -

8.  Create Folders and Files required for project

9.  Git Commit

10. Git Push

11. Git Pull

---

## Outputs:

Ready to start setup for ecommerce project.

---

## Conclusion:

I have learned about the basic setup and development tools integration.
