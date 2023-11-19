# Microk8s - Redis

## Installation
1) Setup Redis [config](./redis-cfg.yaml)

Set `clusterIP` to connect from `pod`s in cluster

2) Install Redis into Microk8s cluster
```bash
microk8s helm repo add bitnami https://charts.bitnami.com/bitnami
microk8s helm repo update
microk8s helm install my-redis bitnami/redis -f redis-cfg.yaml
```

3) Update Redis existing config (optional)
```bash
microk8s helm upgrade my-redis bitnami/redis -f redis-cfg.yaml
```
