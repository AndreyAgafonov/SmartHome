from RemoteHost import RemoteHost


class BaseConfig():
  def __init__(self, _remote_host, _remote_port, _user_login, _user_key_pub):
    self._remote_host = _remote_host
    self._remote_port = _remote_port
    self._user_login = _user_login
    self._user_key_pub = _user_key_pub

  def installBaseSoft(self, base_soft):
    remoteHost = RemoteHost(self._remote_host, self._remote_port, self._user_login, self._user_key_pub)
    remoteHost.execOnRemote("sudo apt-get update -y &>/dev/null")
    remoteHost.execOnRemote("sudo apt-get install %s -y &>/dev/null"
                            % base_soft)
    # hostname="clientr-1"
    #TODO вывести это в конфигурацию приложения
    #TODO сделать в приложении проверку что правильно вводится имя - только англ и только меленькие буковки
    
    # remoteHost.setHostName(hostname)
    #TODO добавить перезагрузку, добавить предупреждение что будет произведена перезагрузка.
                        
  def installClientR(self):
    print('yes')
    remoteHost = RemoteHost(self._remote_host, self._remote_port, self._user_login, self._user_key_pub)

  def configClientR(self):
    print('yes')

  # def replaceMongodConfigAndRestart(self, replacement_config_extension):
  #     remoteHost = RemoteHost(self._remote_host,self._user_login,self._user_key_pub)
  #     remoteHost.execOnRemote("sudo /bin/cp /etc/mongoc.conf.%s /etc/mongoc.conf; bash ./restartMongoC.sh"
  #                             % replacement_config_extension)