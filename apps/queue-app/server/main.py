import os

from fastapi import FastAPI
from celery import Celery
from celery.result import AsyncResult


if CELERY_BROKER_URL := os.getenv('CELERY_BROKER_URL'):
    raise RuntimeError('CELERY_BROKER_URL is not set in env')

if CELERY_RESULT_BACKEND := os.getenv('CELERY_RESULT_BACKEND'):
    raise RuntimeError('CELERY_RESULT_BACKEND is not set in env')


app = FastAPI()
celery_app = Celery(
    __name__,
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post('/process/{s}/{r}')
async def process(s: int, r: int):
    task_id = celery_app.send_task(
        'process',
        kwargs={
            's': s,
            'r': r
        }
    )

    return f'{task_id}'


@app.get('/status/{task_id}')
async def status(task_id: str):
    async_result = AsyncResult(task_id)
    return async_result.status


@app.get('/result/{task_id}')
async def result(task_id: str):
    async_result = AsyncResult(task_id)
    return async_result.result
