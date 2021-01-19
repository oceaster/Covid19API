
# COVID-19 Travel App

View the app in action here <br/>
http://eastercompany.eu.pythonanywhere.com/ <br/>
<br/>
This build is currently untested on Windows or Mac systems. <br/>
Linux (Ubuntu 20.1+) confirmation only.
<br/>
<br/>
Refer: where `python` bash cmd is used you may require `python3` or `python38` <br/>
If you haven't already - you will require pipenv to automatically install dependencies

```bash
python -m pip install pipenv
```
## Quick Guide

1. Refer to Requirements
2. Refer to Install & Setup
3. Refer to Auto Deployment
4. Check the app interface section
5. Check the api input / output section

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

With python 3.8; install the dependencies using the virtual enviroment

```bash
python -m pipenv install
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
python ./manage.py start
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

# WebApp Interface

The application interface and response is quite simple; yet effective.

<table>
    <tr>
        <th> Good Input Example </th>
        <th> Good Result Example </th>
    </tr>
    <tr>
        <td>
            <img width='200px' height='300px'
                src="https://scontent-lhr8-2.xx.fbcdn.net/v/t1.15752-9/140176419_414878859847596_3289243424905538988_n.png?_nc_cat=105&ccb=2&_nc_sid=ae9488&_nc_ohc=TQ5NJBb8DeUAX9Hfmcl&_nc_ht=scontent-lhr8-2.xx&oh=4d8ee57a3c8208833ea9b11a1bbb8e77&oe=602E6337">
        </td>
        <td>
            <img width='200px' height='300px'
                src="https://scontent-lhr8-1.xx.fbcdn.net/v/t1.15752-9/140184718_160323795614996_2106851009253124471_n.png?_nc_cat=111&ccb=2&_nc_sid=ae9488&_nc_ohc=KiWgh-JSidgAX_SwLWb&_nc_ht=scontent-lhr8-1.xx&oh=4abf7faaed49969b705ae9c92739fa9e&oe=602C4C1F">
        </td>
    </tr>
</table>

<table>
    <tr>
        <th> Bad Input Example </th>
        <th> Bad Result Example </th>
    </tr>
    <tr>
        <td>
            <img width='200px' height='320px'
                src="https://scontent-lht6-1.xx.fbcdn.net/v/t1.15752-9/140265205_1044085446077142_6026951136860547900_n.png?_nc_cat=103&ccb=2&_nc_sid=ae9488&_nc_ohc=ZrPC0RYswtcAX_H-iDB&_nc_oc=AQkQ3nq8AuiCOGjsK5Sd0_t8hS2GqPOQHm3JNqIx5ujf2Vty3VhQfIDfJGi8MuzGx-Y&_nc_ht=scontent-lht6-1.xx&oh=51e531bd75f17fe6f2e7b83b0e98db80&oe=602DF2C0">
        </td>
        <td>
            <img width='200px' height='320px'
                src="https://scontent-lhr8-2.xx.fbcdn.net/v/t1.15752-9/140197409_778329102767712_3269018544921037580_n.png?_nc_cat=102&ccb=2&_nc_sid=ae9488&_nc_ohc=7BCyih1NQ1AAX8dxuQQ&_nc_ht=scontent-lhr8-2.xx&oh=63a3bf3431f0ecbed4e8d0ae75c8bfbc&oe=602AE9AE">
        </td>
    </tr>
</table>

you can view this application is production by
[clicking here!](https://eastercompany.eu.pythonanywhere.com/)

# API Input / Output

To recieve a response in JSON with boolean status for each condition and warnings
on failures or conditional circumstances use this endpoint with 'return_date' as
an optional field.

```
DOMAIN / api / permit / <location> / <destination> / <age> / <travel_date> / <return_date>
```

an example input would be as follows:

```
/api/permit/united-kingdom/united-states/18/2021-1-23/2021-1-25
```

an example response would be as follows:

```
{
    "travel_date": true,
    "return_date": true,
    "age": true,
    "loc_to_des": true,
    "warnings": ["must travel with adult"]
}
```

`travel_date` confirms travel date is within 2-5 workings days. <br/>
`return_date` confirms return date is within 2 months if applicable. <br/>
`age` returns applicable travel age (21+) or (15+ with a warning atached). <br/>
`loc_to_des` as in location to destination confirms loc cases are lower than des cases.
<br/>
`warnings` contains any information on failures or extra information such as when a user
is between the age of 15 and 21 and can travel only if supervised by an adult.
<br/>

You can interact with this api on this URL:<br/>
https://eastercompany.eu.pythonanywhere.com<br/>
<br/>
Here is an example query you can sample.<br/>
https://eastercompany.eu.pythonanywhere.com/api/permit/united-kingdom/united-states/18/2021-1-23/2021-1-25<br/>

<br/>
<br/>
<p align='center'> By </p>
<p align='center'> Owen Cameron Easter </p>
<p align='center'> For </p>
<p align='center'> <a href='https://profusion.com/'> ProFusion </a> </p>
