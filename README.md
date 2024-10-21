## Project Setup

Start by cloning this repository, and `cd` into it.

If you are running this app for the first time, it is a good idea to first create a virtual environment. To do so, at the root of this project, run
```bash
python -m venv djangovenv
```
where the `-m` option is used to execute a specific Python module.  

Now, activate your virtual environment with
```bash
source djangovenv/bin/activate
```

Now, whenever you want to exit the virtual environment, run `deactivate`.

You are now ready to install the dependencies of this project by running
```bash
pip install -r requirements.txt
```

Next, set up the database with `sqlite3 db.sqlite3 < dump.sql`.

You can now start the development server with `python manage.py runserver`, which by default will run the app on port 8000.


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
