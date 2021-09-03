import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ContactSys.settings')

app = Celery('ContactSys')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Function will execute the crawler every day at 9:30 AM
    command for a help: celery -A exec_crawler worker -l info -B
    """
    sender.add_periodic_task(crontab(hour='*/1'), exec_func.s(), name='call every minute')

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')