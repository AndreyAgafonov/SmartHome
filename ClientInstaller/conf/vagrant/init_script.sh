#!/bin/bash
username=ubuntu



useradd $username
mkdir -p /home/$username/.ssh/
cat /vagrant/conf/vagrant/ssh_key.pub >/home/$username/.ssh/authorized_keys
chown -R $username:$username /home/$username
apt-get update -y 1>/dev/null && apt-get install mc -y 1>/dev/null


systemctl stop ufw
systemctl disable ufw