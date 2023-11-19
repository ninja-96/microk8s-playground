# Microk8s - Nvidia Triton Server

## Installation
1) Edit [manifest](./manifest.yaml)

Change IP-address from `10.152.183.201` to yours

2) Enable `Nvidia GPU` in Microk8s cluster
```bash
microk8s enable gpu
```

> _**Node:** You need to install `Nvidia Driver` and `Nvidia Container Toolkit` - [link](https://microk8s.io/docs/addon-gpu#use-host-drivers-and-runtime-4)_
