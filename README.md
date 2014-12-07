Grocery list test application
=============================

Requirements
------------

 - Django (tested with version 1.7.1)
 - Python 3 (tested with version 3.4.2)
 
 Tested only on a Linux box (Ubuntu 14.10).

Installation
------------

 - `git clone git@github.com:uaraven/grocery.git`
 - `cd grocery`
 - `python3 manage.py migrate`
 - `python3 manage.py test`
 - `python3 manage.py runserver`
 - start browser and navigate to `http://localhost:8000/`
 
Deviations from requirements
----------------------------

I used Django built-in SQLite as database, not MySQL or PostgreSQL, 
but given the fact that it is zero-configuration solution I hope it will cause no problems.

I am neither Web-designer nor Javascript developer, so web interface is quite rudimentary.

Features to be added
--------------------
 
  - Authentication. I initially added Django auth module, but did not implemented authentication, because I already missed all deadlines.
  - API Key support for APIs. Also Web page to generate API keys for users. Currently APIs are unprotected and open to the world.
  - Mobile client. Should be pretty easy with JSON APIs available.
