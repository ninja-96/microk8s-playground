import os
import socket
from fastapi import FastAPI

import numpy as np


app = FastAPI()


@app.get("/")
async def root():
    return "Hello, World!"


@app.get('/ip')
async def ip():
    return f'{socket.gethostbyname(socket.gethostname())}'


@app.get('/listdir')
async def listdir():
    return os.listdir('/mnt')


@app.get('/predict/{size}/{repeats}')
async def predict(size: int, repeats: int):
    for _ in range(repeats):
        x = np.random.random((size, size)).astype(np.float32)
        y = np.random.random((size, size)).astype(np.float32)

        a = x + y
        b = y - x
        c = x / y
        d = y * x
        e = np.mean(x + y / a * b - c)
    
    return f'{e}'
