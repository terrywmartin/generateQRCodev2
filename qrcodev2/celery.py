import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qrcodev2.settings')

app = Celery('qrcodev2')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(result_expires=3600,
                enable_utc=True,
                timezone='US/Central' )

app.autodiscover_tasks()

