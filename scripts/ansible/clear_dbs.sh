#!/bin/bash
chmod 0600 /vagrant/ansible.pem
all_dbs=(mdb-torin mdb-balin mdb-dvalin mdb-bifur mdb-gloin mdb-nori mdb-bombur mdb-fili mdb-kili)
echo -e "\e[91m Clear DBS folder\033[0m"
for target_host in ${all_dbs[*]}
do
  echo -e "Clear data on $target_host" |awk -F% '{printf "%-30s", $1 }'
  ssh -q -o "StrictHostKeyChecking no" vagrant@${target_host} -i /vagrant/ansible.pem 'sudo systemctl stop mongod && sudo rm -rf /datadrive && sudo rm -f /etc/mongod.conf'
    if [[ $? == 0 ]]
    then
      printf '\e[7;32m%-6s\e[m' "Clered\n"
    else
      printf '\e[7;31m%-6s\e[m'  "Error\n"
  fi
done


#\e[m
#printf '\e[91;34m%-6s\e[m' "This is text"