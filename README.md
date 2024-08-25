## Project Setup

Start by cloning this repository, and `cd` into it.

If you are running this app for the first time, I recommend you start by creating a virtual environment in a directory of your choice. For example:
```bash
python -m venv ~/.virtualenvs/djangodev
```
where the `-m` option is used to execute a specific Python module.  
If you do not yet have a `~/.virtualenvs` directory, just make sure to create one first.  

Now, activate your virtual environment with
```bash
source ~/.virtualenvs/djangodev/bin/activate
```
If you put the virtual environment in another directory, just adjust the path accordingly.

When you want to exit the virtual environment, use `deactivate`

You are now ready to install the dependencies of this project by running
```bash
pip install -r requirements.txt
```

Next, set up the database with `sqlite3 db.sqlite3 < dump.sql`.

To run the development server: `python manage.py runserver`


## OWASP

The task was to include at leat 5 different flaws from the [OWASP top 10 list](https://owasp.org/www-project-top-ten/):
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

In addition to these 10 flaws, [cross-site request forgery](https://www.cloudflare.com/learning/security/threats/cross-site-request-forgery/) was also allowed.
