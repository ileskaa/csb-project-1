"""
ASGI (Asynchronous Server Gateway Interface) config for csbproject1 project.

ASGI, a successor to WSGI, is an emerging standard for asynchronous web servers and applications.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csbproject1.settings')

application = get_asgi_application()
