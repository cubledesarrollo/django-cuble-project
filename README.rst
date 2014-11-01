====================
django-cuble-project
====================

A project template for Django 1.7.

To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using the django-cuble template
#. Install additional dependencies
#. Use the Django admin to create the project

*note: these instructions show creation of a project called "potato". You
should replace this name with the actual name of your project.*

Working Environment
===================

You have several options in setting up your working environment. We recommend
using virtualenv to separate the dependencies of your project from your system's
python environment. If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv --distribute potato

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

Virtualenv with virtualenvwrapper
---------------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you::

    $ mkdir potato
    $ mkvirtualenv -a potato potato-dev
    $ cd potato && add2virtualenv `pwd`

Using virtualenvwrapper with Windows
------------------------------------

There is a special version of virtualenvwrapper for use with Windows (https://pypi.python.org/pypi/virtualenvwrapper-win).::

    > mkdir potato
    > mkvirtualenv potato-dev
    > add2virtualenv potato


Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django

Creating your project
=====================

To create a new Django project called '**potato**' using
django-cuble-project, run the following command::

    $ django-admin.py startproject --template=https://github.com/theroomofcode/django-theroomofcode-project/archive/master.zip --extension=py,rst,html,less,coffee potato_project

Installation of Dependencies
============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

