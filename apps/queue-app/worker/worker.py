import os

import numpy as np
from celery import Celery


CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')


if not CELERY_BROKER_URL or not CELERY_RESULT_BACKEND:
    raise RuntimeError()


celery_app = Celery(
    __name__,
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL
)


@celery_app.task(name='process')
def process(s, r):
    x = np.random.random((s, s, s)).astype(np.float32)
    y = np.random.random((s, s, s)).astype(np.float32)

    for i in range(r):
        a = x + y
        b = y - x
        c = x / y
        d = x * y
        e = a + b - c / d + x / y

    return f'{np.mean(e)}'
