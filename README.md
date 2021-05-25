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
```
(venv)$ python manage.py runserver
```
And navigate to http://127.0.0.1:8000.
