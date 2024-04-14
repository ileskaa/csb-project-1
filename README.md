Activate your virtual environment with
`source ~/.virtualenvs/djangodev/bin/activate`

Deactivate it with `deactivate`

Run the development server: `python manage.py runserver`

https://docs.djangoproject.com/en/5.0/intro/tutorial01/

https://cybersecuritybase.mooc.fi/module-3.1

## Directory Structure

`manage.py` is a command-line utility that lets you interact with this Django project.

The `csbproject1` directory is the actual Python package for the project. You will have to use its name to import anything inside it. E.g., `mysite.urls`

## OWASP

Must have at leat 5 different flaws from the [OWASP top 10 list](https://owasp.org/www-project-top-ten/):
1. Broken access control
2. Cryptographic failures
3. Injection
4. Insecure design
5. Security misconfiguration
6. Vulnerable and outdated components
7. Identification and authentication failures
8. Software and data integrity failures
9. Security logging and monitoring failures
10. Server-side request forgery
