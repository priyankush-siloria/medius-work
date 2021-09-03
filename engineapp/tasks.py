from demoapp.models import Widget

from celery import shared_task



@shared_task
def exec_func():
	print("Holaaaaaa!!!!!!!!!!!!!!!!!!!!!!!!11")