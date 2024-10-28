# Microk8s Playground

## Installation
- Setup
    - [Setup OS and Snapd](#setup-os-and-snapd)
    - [Setup node](#setup-node)
- [Add new node](#add-new-node-to-cluster)
- [Setup NFS server](#setup-nfs-server)
- Extra
    - [Apply manifest with image from Microk8s registry](#apply-manifest-with-image-from-microk8s-registry)
- Apps
    - [AI app](#ai-app)
    - [Queue app](#queue-app)

### Setup OS and Snapd
1) Install Ubutnu, Debian Linux OS
2) Install snapd daemon 

Follow instructions in this [link](https://snapcraft.io/docs/installing-snapd) to install Snapd

3) Install Microk8s [link](https://microk8s.io/), [script](./scripts/install_microk8s.sh)
```bash
apt install iptables-persistent
snap install microk8s --classic
```

Add your user into `microk8s` group
```bash
usermod -a -G microk8s <your-user-name>
mkdir ~/.kube
chown -R <your-user-name> ~/.kube
systemctl reboot
```

Check Microk8s setup
```bash
microk8s status --wait-ready
microk8s kubectl get all --all-namespaces
```

> _**Note:** If you use microk8s registry enable `cgroups`_

### Setup node
1) Follow [instructions](#setup)
2) Enable Microk8s services

Run commands or run [script](./scripts/config_node.sh)
```bash
microk8s enable dashboard
microk8s enable dns
microk8s enable metrics-server
```

Restart Microk8s
```bash
microk8s stop
microk8s start
```

## Add new node to cluster
1) Edit `/etc/hosts` on main node
```bash
nano /etc/hosts
```

2) Add new node IP address and hostname on main node
```
192.168.10.3	k8s-rpi4-1-node
```

3) Run command on main node and follow instructions
```bash
microk8s add-node
```

4) Check updated nodelist on main node
```bash
kubectl get nodes
```

## Setup NFS server
1) Install NFS server
```bash
apt install nfs-kernel-server
```

2) Create directory for storage
```bash
mkdir -p /nfs
mkdir -p /nfs/data
mkdir -p /nfs/models
```

3) Add rules to `/etc/exports`
```
/nfs  192.168.10.0/24(rw,async,fsid=0,no_subtree_check)  # only access from 192.168.10.0 network
```

4) Update exports table
```bash
exportfs -a
```

5) Start server
```bash
systemctl enable nfs-server
```

6) On client run command
```bash
apt install nfs-common
```

7) Connect from client PC to NFS server
```bash
mount <nfs-server-ip-address>:/data /mnt/nfs/data
mount <nfs-server-ip-address>:/models /mnt/nfs/models
```

> _You can use manifects from [directory](./pvc/) to connect NFS server to Microk8s cluster_


## Extra
### Apply manifest with image from Microk8s registry

1) Build and push Docker image to Microk8s registry server
```bash
docker build . --push -t <micro8ks-registry-ip-address>:32000/<image-name>:<image-tag>
```

2) Load image to Mi
```bash
microk8s ctr image pull --plain-http  <micro8ks-registry-ip-address>:32000/<image-name:image-tag>
```

3) Create `deployment.yaml` manifect and apply them
```bash
kubectl apply -f deployment.yaml
```

> _**Note:** More details [here](https://microk8s.io/docs/registry-built-in)_


## Apps
- [AI app](./apps/ai-app/)
- [Queue app](./apps/queue-app/)
