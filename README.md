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

## Setup

If you are already here, you have access to the [Github repository](https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git). Clone the repository to your local machine.

```bash
$ git clone https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git
```

In the repository, you will find a ``requirements.txt`` file. Use this to create a virtual envirnoment for texting the Django project locally.
However, since the project uses postgres DBMS, you will have to set this up locally. See [postgres local setup](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup) for instructions.
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

Depending on your edits you may have to run some of these commands during development. Before deployment it is best to test heroku locally. To do this, install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) and use the follwing command instead of ``python manage.py runserver``:
```bash
(djangoVenv) SwarnamruthaPrasanaApp $ heroku local -f Procfile.windows
```
Once heroku is setup and you are logged in to heroku using ``$ heroku login``, it is possible to ``$ git push heroku master`` all commited changes on local master branch. 
However, you may not have access to do this. 
In that case, the best way to collaborate is by commiting changed to a new local branch, pushing the branch upstream to the [Github repository](https://github.com/NandithaMudunuru/SwarnamruthaPrasanaApp.git) and creating a pull request to repository master. People with access to the heroku deployed site will verify the changes and push to heroku master.