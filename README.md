

<h1 align="center">Restful Authentication API


<p align="center">

[![Django CI](https://github.com/decadevs/week-9-task-python-samsonosiomwan/actions/workflows/ci.yml/badge.svg)](https://github.com/decadevs/week-9-task-python-samsonosiomwan/actions/workflows/ci.yml)

</p>
</h1>
<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Week 9 Task Python SAMSON OSIOMWAN  🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#anchor-api-calls">API Calls</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/samsonosiomwan" target="_blank">Author</a> |
   <a href="https://decagon-user-auth-api.herokuapp.com" target="_blank">View APP ON HEROKU</a>
</p>

<br>

## :dart: About ##

A full authentication API that can be used in any application.

## :sparkles: Features (endpoints) ##

:heavy_check_mark: Registration ;\
:heavy_check_mark: Generate OTP ;\
:heavy_check_mark: Verify OTP ;\
:heavy_check_mark: Login ;
:heavy_check_mark: Logout ;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Django Framework](https://www.djangoproject.com)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [heroku hosting]
- [heroku ci/cd]

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python3+](https://www.python.org/downloads/), [PostgreSQL](https://www.postgresql.org/download/) installed.

Note: .env file has to be created in root directory with the following keys and values for setting postgresql database.

```text
NAME=db_name
USER=db_user
PASSWORD=db_password
PORT=5432
```

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/decadevs/week-9-task-samsonosiomwan.git

# Access
$ cd week-9-task-python-samsonosiomwan

# Install virtual env
$ python -m venv venv

# Start virtual env
$ . venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Makemigrations
$ python manage.py makemigrations --settings=auth_api_project.settings.development

# Migrate
$ python manage.py migrate --settings=auth_api_project.settings.development

# Run the project
$ python manage.py runserver --settings=auth_api_project.settings.development

# The server will initialize in the <http://localhost:8000>
```

## :anchor: API Calls ##

API Documentation

```text
http://127.0.0.1:8000/
```
```text
https://decagon-user-auth-api.herokuapp.com
```

Registration

This register new user into database using registration details passed by the user.

```text
http://127.0.0.1:8000/auth-api/v1/register/

```
```text
https://decagon-user-auth-api.herokuapp.com/auth-api/v1/register/

```

Generating OTP

This generate 6 numeric time-based OTP base on the email a user register with, and sends the generated OTP to user email for verification

```text
http://127.0.0.1:8000/auth-api/v1/generate-otp/
```
```text
https://decagon-user-auth-api.herokuapp.com/auth-api/v1/generate-otp/

```
Verify OTP

This verifies OTP sent to user and make his account active for login

```text
http://127.0.0.1:8000/auth-api/v1/verify-otp/
```
```text
https://decagon-user-auth-api.herokuapp.com/auth-api/v1/verify-otp/

```

Login Token

This ask for active user login details, verify user and return Django Rest Framework token.

```text
http://127.0.0.1:8000/auth-api/v1/login-token/
```
```text
https://decagon-user-auth-api.herokuapp.com/auth-api/v1/login-token/

```


Made with :heart: by <a href="https://github.com/samsonosiomwan" target="_blank">Samson Osiomwan</a>

&#xa0;

<a href="#top">Back to top</a>
