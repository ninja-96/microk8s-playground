FROM ubuntu:jammy

WORKDIR /app

RUN apt update -y
RUN apt upgrade -y;
RUN apt install python3-pip -y;

COPY requirements.txt /app
COPY worker.py /app

RUN pip3 install --no-cache-dir -r requirements.txt
