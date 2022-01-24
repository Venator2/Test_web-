## Local run 

```sh
$ cd app
$ sudo pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```