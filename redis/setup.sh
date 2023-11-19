#! /bin/bash

microk8s helm repo add bitnami https://charts.bitnami.com/bitnami
microk8s helm repo update
microk8s helm install my-redis bitnami/redis -f redis-cfg.yaml
