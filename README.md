# Swarnamrutha Prasana Website

A site to support swarnamrutha prasana events conducted by Vikasatarangini and JIMS Auyurveda NIlayam. The site handles attendee registration forms, events schedules, venues and coordinators.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git)


---------

## Developer Guide 

### Windows 10

#### Code: Cloning the git repository

If you are already here, you have access to the [Github repository](https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git). Clone the repository to your local machine.

```bash
$ git clone https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git
```

#### Development: Python & virtual environment

Since the project is based on python-Django, you have to setup Python >= 3.10.4. 
Checkout this easy to follow [guide](https://realpython.com/installing-python/) to verfiy your python version or setup it up. 
Once verified, setup a virtual environment for the project. 
While there are many ways to set it up, I like to have all my virtual environments in one location. 
I start by creating a ``.venvs`` folder in ``C:\Users\<user>\`` and then creating all virutal environemnts within that folder. 
```bash
$ python -m venv C:\Users\<user>\.venvs\<NameForCurrentProjectVenv>
``` 
and activate it
```bash
$ C:\Users\<user>\.venv\<NameForCurrentProjectVenv>\Scripts\activate
```
With the virtual environment activated, use the ``requirements.txt`` file from the cloned git repository to install all the dependencies for testing this Django project locally.
```bash
(NameForCurrentProjectVenv) SwarnamruthaPrasanaApp $ pip install -r requirements.txt
```

#### DBMS: Postgres

Since the project uses postgres DBMS, you will have to set this up locally. See [postgres local setup](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup) for instructions.
During the setup, you will be asked to define the following:

* Database Name
* User Name
* Password
* Host
* Port

Use the credentials from the ``SwarnamruthaPrasanaApp/SwarnamruthaPrasana/settings.py`` file: 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres', # Database Name
        'USER': 'postgres', # User Name
        'PASSWORD': 'JaiSrimanNarayana', # Password
        'HOST': 'localhost', # Host
        'PORT': '5432', # Port
    }
}
```

This way there is no need to tweak the settings file. You will now have to migrate the models to the database. But before doing that since this site uses database cache you need to create a cache table.
```bash
(djangoVenv) SwarnamruthaPrasanaApp $ python manage.py createcachetable
(djangoVenv) SwarnamruthaPrasanaApp $ python manage.py makemigrations
(djangoVenv) SwarnamruthaPrasanaApp $ python manage.py migrate
```
With this you can now locally run the site without heroku. You can also create a django ``superuser`` to do some admin work or change permissions for any dummy users you create for testing.

Finally, you need to compress and collect all the static files before you run the server.
```bash
(djangoVenv) SwarnamruthaPrasanaApp $ python manage.py compress
(djangoVenv) SwarnamruthaPrasanaApp $ python manage.py collectstatic
(djangoVenv) SwarnamruthaPrasanaApp $ python manage.py runserver
```

Depending on your edits you may have to run some of these commands during development.

#### Deployment: Heroku

The website is deployed vis Heroku. 
So before deploying chnages, it is best to test heroku locally. 
Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) and use the following command instead of ``python manage.py runserver`` to run local server:
```bash
(djangoVenv) SwarnamruthaPrasanaApp $ heroku local -f Procfile.windows
```
If the changes are ready for deployment, log in to heroku using ``$ heroku login`` and push all commited changes from local master branch to heroku master. 
```bash
(djangoVenv) SwarnamruthaPrasanaApp $ git push heroku master
```
However, you may not have access to do this. 
In that case, the best way to collaborate is by creating a new local branch:
```bash
$ git checkout -b <newBrachForChanges>
```
to make necessary changes. After testing the changes on local server, commit them to the local branch and push the branch upstream to the [Github repository](https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git). 
```bash
$ git add .
$ git commit -m "<Comments for the commits>"
$ git push -u origin <newBrachForChanges>
```
Then visit the [Github repository](https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git) and create a pull request to merge the changes with the master branch. People with access to deploy the site on heroku will verify the changes and push to heroku master.


---------

## License & copyright

[![License : GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp/blob/master/LICENSE)

Copyright (C) 2022 [Nanditha Mudunuru](www.linkedin.com/in/nmudunuru), [Vikasa Tharangini](https://vtsbharath.org/aboutus/)
