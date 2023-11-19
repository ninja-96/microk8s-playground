#! /bin/bash

snap install microk8s --classic -y;
usermod -a -G microk8s $USER;
mkdir ~/.kube
chown -R $USER ~/.kube
systemctl reboot
