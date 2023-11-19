#! /bin/bash

microk8s enable dashboard
microk8s enable dns
microk8s enable metrics-server
microk8s stop
microk8s start
