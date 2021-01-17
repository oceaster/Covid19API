
# COVID-19 Travel App

View the app in action here
[eastercompany.eu.pythonanywhere.com](http://eastercompany.eu.pythonanywhere.com/) <br/>

This build is currently untested on Windows or Mac systems. <br/>
Linux (Ubuntu 20.1+) confirmation only. <br/>
<br/>
Refer: where python cmd is used you require python3 or python38

```bash
>> python
```

```bash
>> python3
```

```bash
>> python38
```

## Quick Guide

1. Refer to Requirements
2. Refer to Install & Setup
3. Refer to Auto Deployment

## Challenge Summary

This is a Django Web Developer Technical Assessment for Profusion

### Instructions

In this test we will use Covid19 API https://documenter.getpostman.com/view/10808728/SzS8rjbc.
Your main task will be creating a web client form and an API endpoint for travel permit
inquiries using Django. Your API must consider the following conditions.

#### Input data

Your API must take the following fields as input:

1. Date of travel
2. Date of return (optional)
3. Country of origin
4. Country of destination
5. Age of traveller

#### Things to be checked:

 1. Date of travel is between next 2 and 5 following working days from date of request. Otherwise, the travel permit must be denied.
 2. If Date of return is present, and date of return is within 2 months of the Date of travel, then the travel can be approved. In any other case the travel permit must be denied.
 3. Country of origin and Country of destination must be valid country names.
 4. Travel is only a llowed from countries where numberof Covid cases in Country of origin is lower than in the Country of destination.
 5. Travel is only allowed for travellers older than 21 and younger than 65. However, if traveller is older than 15 years old, he/she can travel with supervision of an adult. (You must show this prompt in your output when appropriate)

## Requirements

<div>
    <a href='https://www.python.org/downloads/release/python-387/'>
        <img
            alt='Python'
            src='https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png'
            width='64px'
            height='64px'
        />
        <p> Python 3.8 </p>
    </a>
<div>

## Install & Setup

With python 3.8 install the dependencies using the virtual enviroment

```bash
python -m pipenv install
```

or if you have multiple versions of python installed you might need

```bash
python38 -m pipenv install
```

you may wish to install dev dependencies if you intend of modifying this build

```bash
python -m pipenv install -d
```

The required depenencies are as follows

1. Django 2.2.11
2. Django-rest-framework
3. Django-cors-headers
4. PyTest
5. PyTest-Django

The additional dev dependencies; which are not required.

1. Pylint

We use PyTest as a required dependency as this tests API status and functionality
of which this app is dependent on - unit tests are run automatically by the auto-deploy
method listed below in the deployment section.

## Testing

Enter your pipenv virtual enviroment shell by running

```bash
python -m pipenv shell
```

Our unit tests are written with PyTest and all tests can be run with the following

```bash
pytest
```

## Auto Deployment

The auto deployment method will

1. Run unit tests before deploying.
2. Automatically make migrations
3. Automatically apply migrations
4. Make your life a little bit easier

<br/>
Enter your pipenv virtual enviroment shell by running

```bash
python -m pipenv shell
```

By default the server will be hosted on <b>http://localhost:8000/</b><br/>
and can be started by running the following command line within the shell.

```bash
./manage.py start
```

## Manual Deployment

The manual deployment method will

1. Not run unit tests before deploying.
2. Not make migrations
3. Not apply migrations
4. Not make your life a little bit easier

<br/>
Enter your pipenv virtual enviroment shell by running

```bash
python -m pipenv shell
```

First you will need to build the database

```bash
python ./manage.py makemigrations
```

then apply migrations

```bash
python ./manage.py migrate
```

test that the database and api are communicating appropriately

```bash
pytest
```

By default the server will be hosted on <b>http://localhost:8000/</b><br/>
and can be started by running the following command line within the shell.

```bash
python ./manage.py runserver
```

<br/>
<br/>
<p align='center'> By </p>
<p align='center'> Owen Cameron Easter </p>
<p align='center'> For </p>
<p align='center'> <a href='https://profusion.com/'> ProFusion </a> </p>
