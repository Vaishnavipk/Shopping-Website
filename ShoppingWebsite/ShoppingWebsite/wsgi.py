"""
WSGI config for ShoppingWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ShoppingWebsite.settings")

from blog.settings import DEBUG

application = get_wsgi_application()


if not DEBUG:    # Running on Heroku
    from dj_static import Cling
    application = Cling(get_wsgi_application()