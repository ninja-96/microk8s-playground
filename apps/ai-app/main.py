import os
import socket
from fastapi import FastAPI

import torch
import torchvision


app = FastAPI()
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = torchvision.models.resnet50(weights='DEFAULT').eval().to(device)


@app.get("/")
async def root():
    return "Hello, World!"


@app.get('/ip')
async def ip():
    return f'{socket.gethostbyname(socket.gethostname())}'


@app.get('/listdir')
async def listdir():
    return os.listdir('/mnt')


@app.get('/predict/{batch_size}/{size}/{repeats}')
async def predict(batch_size: int, size: int, repeats: int):
    with torch.inference_mode():
        x = torch.rand(batch_size, 3, size, size).to(device)
        for _ in range(repeats):
            r = model(x)
    
    return f'{torch.argmax(r, 1)}'
