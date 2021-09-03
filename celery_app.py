from celery import Celery
from celery.schedules import crontab
import os
import requests
import json

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Function will execute the crawler every day at 9:30 AM
    command for a help: celery -A exec_crawler worker -l info -B
    """
    sender.add_periodic_task(crontab(hour='*/1'), exec_func.s(), name='call every minute')


@app.task
def exec_func():
	headers = {'Conetent-Type': 'application/json'}
	response_data = requests.post('http://127.0.0.1:8000/api/request/',data={"requested_url":"http://127.0.0.1:8000/api/get/2/"}, headers=headers)