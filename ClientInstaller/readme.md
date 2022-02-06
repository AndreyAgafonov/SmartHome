## Init dev env

```bash
vagrant up
vagrant ssh  -- -t 'sudo  bash -c /vagrant/conf/vagrant/init_script.sh'
```



## Remove dev env
```bash
 vagrant destroy -f
```