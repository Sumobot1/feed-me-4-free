from __future__ import absolute_import

import os
import django

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedme4free.settings')
django.setup()

app = Celery('feedme4free')

app.config_from_object('django.conf:settings')
#app.autodiscover_tasks(lambda: [n.name for n in django.apps.get_app_configs()])