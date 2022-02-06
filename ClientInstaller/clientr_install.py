import configparser as configparser
import time
import datetime, time
import paramiko
from RemoteHost import RemoteHost
from BaseConfig import BaseConfig
# from ConfigPlusRouter import ConfigPlusRouter
# from Shard import Shard


print("Config ClientR - Task: 1 Configuration")
parser = configparser.ConfigParser()
parser.read('conf/properties.ini')
sections = parser.sections()

# remoteHostShards = {}
# remoteHostConfig = None
# renameReplicaSets = {}



for i, section in enumerate(sections):
    if section == "general":
        keyfile = open(parser[section]['user_pub_key'])
        key = paramiko.RSAKey.from_private_key(keyfile)
        __ssh_remote_host = parser[section]['remote_host']
        __ssh_remote_port = parser[section]['remote_port']
        __ssh_user_login = parser[section]['user_login']
        __ssh_user_pub_key = key
        # parser[section]['user_pub_key']
        __base_soft = parser[section]['base_soft']
        createBaseConfig = BaseConfig( __ssh_remote_host, __ssh_remote_port, __ssh_user_login,__ssh_user_pub_key)

createBaseConfig.installBaseSoft(__base_soft)

