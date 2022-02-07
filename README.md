# gtd

> django sqlite3 restapi simpleGtd

## inited env
```shell
sudo apt install python3

python3 --version

sudo apt install sqlite3

sqlite3 --version
```

##  use [python-virualenv](https://virtualenv.pypa.io/en/latest/)
```shell
pip3 install virtualenv

virtualenv gtd

source gtd/bin/activate

pip3 install django djangorestframework
```

##  init django proj
```shell
cd gtd

django-admin startproject toDoList

cd toDoList

python3 manage.py startapp mainApp
```

##  Coding
```python
# TODO coding ！！！！
```

## Run server
```shell
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver
```

## Test RestApi
> open browser, and test apis
```html
http://localhost:8000/

http://localhost:8000/api

http://localhost:8000/api/create/

http://localhost:8000/api/1/

http://localhost:8000/api/delete/1
```

## Create admin users
> create admin user and password
```
python3 manage.py createsuperuser
```
> my shell infos
```html
$ python3 manage.py createsuperuser</br>
Username (leave blank to use 'panshi'): 
Email address: panshi@gtd.com  
Password:  
Password (again):  
This password is too short. It must contain at least 8 characters.  
This password is too common.  
This password is entirely numeric.  
Bypass password validation and create user anyway? [y/N]: y  
Superuser created successfully.  
```

## Run server
```shell
python3 manage.py runserver
```
## Test as website
> open browser
```html
http://localhost:8000/admin
```

## OTHERS
- [PDM - Python Development Master](https://pdm.fming.dev/)
- [pipx — Install and Run Python Applications in Isolated Environments](https://pypa.github.io/pipx/)
