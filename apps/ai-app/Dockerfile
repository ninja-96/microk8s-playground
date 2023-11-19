FROM ubuntu:jammy

RUN apt update -y;
RUN apt upgrade -y;

RUN apt install python3-pip -y;
RUN pip3 install -U pip;

COPY . .
RUN pip3 install -r requirements.txt
