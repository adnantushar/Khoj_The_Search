# Khoj_The_Search
## Setup
The first thing to do is to clone the repository:
```
$ git clone https://github.com/adnantushar/Khoj_The_Search.git
$ cd Khoj_The_Search
```
Create a virtual environment to install dependencies in and activate it:
```
$ virtualenv venv
$ source venv/bin/activate
Or Try 
$ py -m venv venv
$ venv/Scripts/activate
```
Then install the dependencies:
```
(env)$ pip install -r requirements.txt
```
Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.
Once pip has finished downloading the dependencies:

Creating admin user:
```
(venv)$ python manage.py createsuperuser
```
```
(venv)$ python manage.py runserver
```
And navigate to http://127.0.0.1:8000.

Admin page http://127.0.0.1:8000/admin.

## Walkthrough
After successfully run server you can access api also.

### List Of API Endpoint:

Search List Of Input Values and Number: Api endpoint:  http://127.0.0.1:8000/api/searchlist Paramater : {'startDateTime':'2021-05-20 17:59:00','endDateTime':'2021-05-25 18:00:00'} Headers : {'Authorization': 'Token token_number'}

User Authentication Token: http://127.0.0.1:8000/api-token-auth Headers : { email, password }

User Regestration:  Api endpoint:  http://127.0.0.1:8000/api/auth/register Paramater : { email, password, first_name, last_name }

User Login: Api endpoint:  http://127.0.0.1:8000/api/auth/login Paramater : { email, password}

User Change Password: Api endpoint:  http://127.0.0.1:8000/api/auth/password_change 

