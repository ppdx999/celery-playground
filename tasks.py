import os
import time
from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
celery.conf.result_backend = os.environ.get('CELERY_BACKEND_URL', 'redis://localhost:6379')

@celery.task
def calc_sum(x: float, y: float) -> float:
    time.sleep(10)
    return x + y
