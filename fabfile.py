#!/usr/bin/python2.7

#import fabric.api 
from fabric.api import *
############## definning guest ip and user name and password

env.hosts=['192.168.1.126','192.168.1.129','192.168.1.131','192.168.1.132']
env.user='vagrant'
env.password='vagrant'

################ defination of function
def webhost():
    sudo("yum install httpd wget unzip zip -y")
    sudo("service httpd start")
    sudo("chkconfig httpd on")
    sudo("service iptables stop")
    sudo("chkconfig iptables off")
    sudo("wget -O web.zip http://www.tooplate.com/download/2097_pop")
    sudo("unzip web.zip")
    with cd("2097_pop"):
        sudo("cp -rvf * /var/www/html/")
        sudo("service httpd restart")
    return



####################### local method #####################

def localinfo():
    local("ls")
