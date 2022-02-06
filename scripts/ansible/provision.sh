#!/bin/bash

#Устанавливаем ansible
apt-get install ansible -y

cd /vagrant/scripts/ansible

chown root:root  /vagrant/ClientInstaller/conf/vagrant/ssh_key
                #  /vagrant/ClientInstaller/conf/vagrant
chmod 600 /vagrant/ClientInstaller/conf/vagrant/ssh_key
ansible-playbook projectX.yml




