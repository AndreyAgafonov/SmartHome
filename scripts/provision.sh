#!/bin/bash

WORKDIR=$(dirname $(readlink -e "$0"))
username=ubuntu

useradd $username
mkdir -p /home/$username/.ssh/
cat $WORKDIR/vagrant/ssh_key.pub >/home/$username/.ssh/authorized_keys
chown -R $username:$username /home/$username
echo -e "$username ALL=(ALL) NOPASSWD:ALL\n" >>/etc/sudoers.d/90_$username

apt-get update -y 1>/dev/null && apt-get install mc -y 1>/dev/null

systemctl stop ufw
systemctl disable ufw
