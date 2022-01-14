# gtd

> django sqlite3 restapi simpleGtd

## inited env

sudo apt install python3

python3 --version

sudo apt install sqlite3

sqlite3 --version

##  use [python-virualenv](https://virtualenv.pypa.io/en/latest/)
pip3 install virtualenv

virtualenv gtd

source gtd/bin/activate

pip3 install django djangorestframework

##  init django proj
cd gtd

django-admin startproject toDoList

cd toDoList

python3 manage.py startapp mainApp
