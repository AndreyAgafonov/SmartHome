#!/bin/bash
chmod 0600 /vagrant/ansible.pem
all_hosts=(
mdb-torin
mdb-balin
mdb-dvalin
mdb-bifur
mdb-gloin
mdb-nori
mdb-bombur
mdb-fili
mdb-kili
gluster-bilbo
gluster-frodo
cer-legolas
cer-tauriel
cer-tranduil
haproxy-radagast
haproxy-gendalf
kibana-elrond
prom-sauron
)

printf  '╔'
for lenght_str in {1..20}; do printf "═"; done
printf '╦'
for lenght_str in {1..21}; do printf "═"; done
printf '╦'
for lenght_str in {1..25}; do printf "═"; done
printf '╦'
for lenght_str in {1..120}; do printf "═"; done
printf "╗\n"

echo -e "\e[1m   -=<Hostname>=-   %-=<SELinux status>=-% -=<Firewalld status>=-  %      -=<Open ports>=- \e[0m" |awk -F"%" '{ printf ("║%-20s║%-21s║%-25s║%-124s║\n", $1, $2, $3, $4) }'

printf  '╠'
for lenght_str in {1..20}; do printf "═"; done
printf '╬'
for lenght_str in {1..21}; do printf "═"; done
printf '╬'
for lenght_str in {1..25}; do printf "═"; done
printf '╬'
for lenght_str in {1..120}; do printf "═"; done
printf "╣\n"

for target_host in ${!all_hosts[@]}
do
  script=$(ssh -q -o "StrictHostKeyChecking no" vagrant@${all_hosts[$target_host]} -i /vagrant/ansible.pem  'sudo  echo -e $(hostname)"%"$(/usr/sbin/getenforce)"%"$( echo "Firewalld is:"$(sudo firewall-cmd --state) )"%"$(sudo firewall-cmd --zone=public --list-ports | head -c 120)')
  echo $script |awk -F"%" '{ printf ("║%-20s|%-21s|%-25s|%-120s║\n", $1, $2, $3, $4 ) }'
done

printf  '╚'
for lenght_str in {1..20}; do printf "═"; done
printf '╧'
for lenght_str in {1..21}; do printf "═"; done
printf '╧'
for lenght_str in {1..25}; do printf "═"; done
printf '╧'
for lenght_str in {1..120}; do printf "═"; done
printf "╝\n"
